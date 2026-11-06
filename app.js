"use strict";
const q=(selector,root=document)=>root.querySelector(selector);
const esc=value=>String(value??"").replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));
function safeUrl(value){try{const u=new URL(value);return u.protocol==="https:"?u.href:""}catch{return ""}}
const map=new maplibregl.Map({container:"map",style:"https://tiles.openfreemap.org/styles/positron",center:[30.304,59.960],zoom:13.2});
map.addControl(new maplibregl.NavigationControl({showCompass:false}),"top-right");
const state={features:[],people:[],marks:[],selected:null,filter:"Все",query:""};
const fallbackImage={
  "SPB-PET-0001":{
    photo_url:"https://commons.wikimedia.org/wiki/Special:FilePath/%D0%9C%D0%B0%D0%BB%D1%8B%D0%B9_%D0%9F%D0%A1_1%D0%91_01.jpg?width=960",
    photo_author:"Екатерина Борисова",
    photo_license:"CC BY-SA 4.0",
    photo_license_url:"https://creativecommons.org/licenses/by-sa/4.0/",
    photo_source_url:"https://commons.wikimedia.org/wiki/File:Малый_ПС_1Б_01.jpg",
    photo_status:"LICENSE_VERIFIED",
    preview_note:"Фото включено как отдельный исследовательский медиакандидат; каноническая запись не менялась."
  }
};
function displayData(p){return p.id==="SPB-PET-0001"?{...p,...fallbackImage[p.id]}:p}
function markUrl(f){const url=new URL(window.location.href);url.searchParams.set("place",f.properties.id);history.replaceState(null,"",url.pathname+url.search+url.hash)}
function showing(){return state.features.filter(f=>{const p=f.properties;return (state.filter==="Все"||p.category===state.filter)&&[p.name,p.address,p.description,p.look].join(" ").toLocaleLowerCase("ru").includes(state.query)})}
function renderSearch(){const found=showing(),results=q("#results-list");q("#search-count").textContent=found.length;q("#places-count").textContent=state.features.length+" места";results.replaceChildren();for(const f of found){const p=f.properties,b=document.createElement("button");b.className="result-item"+(state.selected===p.id?" active":"");b.type="button";const title=document.createElement("strong"),sub=document.createElement("small");title.textContent=p.name;sub.textContent=p.address||"";b.append(title,sub);b.onclick=()=>selectPlace(f);results.append(b)}if(!found.length){const none=document.createElement("p");none.className="search-note";none.textContent="Ничего не найдено";results.append(none)}}
function renderMarkers(){for(const m of state.marks)m.remove();state.marks=[];showing().forEach((f,i)=>{const p=f.properties;const button=document.createElement("button");button.className="marker"+(state.selected===p.id?" selected":"");button.type="button";button.textContent=String(i+1);button.setAttribute("aria-label","Открыть "+p.name);button.title=p.name;button.onclick=()=>selectPlace(f);state.marks.push(new maplibregl.Marker({element:button}).setLngLat(f.geometry.coordinates).addTo(map))})}
function renderAll(){renderSearch();renderMarkers()}
function personMarkup(x){const type=({RESIDED_AT:"Проживание",OWNED_PROPERTY_AT:"Владение",ACQUIRED_PARCEL:"Приобретение участка"})[x.relation_type]||"Историческая связь";
let date=x.valid_from?("с "+esc(x.valid_from)):"начало не установлено";if(x.valid_to)date+=" · до "+esc(x.valid_to);
switch(x.date_precision){
  case "DEPARTURE_YEAR_ONLY":date="Выбыл в "+esc(x.valid_to)+" году · начало неизвестно";break;
  case "DIRECTORY_EDITION_YEAR":date="Упомянут в справочнике "+esc(x.valid_to)+" года (не срок владения)";break;
  case "YEAR_CONTEXT_ONLY":date="Дата "+esc(x.valid_to)+" относится к контексту здания, не к периоду владения";break;
  case "OBSERVED_1934_ONLY":date="Зафиксирован в материалах за 1934 год";break;
  case "DAY_ACQUISITION_ONLY":date="Приобретение участка: "+esc(x.valid_from);break;
  case "UPPER_BOUND_ONLY":date="Указано проживание до "+esc(x.valid_to)+" года; начало неизвестно";break;
  case "YEAR_RANGE_COMPOSITE_SOURCES":date=esc(x.valid_from)+"–"+esc(x.valid_to)+" (разные источники, период требует сверки)";break;
}
let url=safeUrl(x.source_url);return '<div class="person"><b>'+esc(x.person_name)+'</b><small>'+esc(type)+' · '+esc(x.historical_address)+(x.apartment?" · кв. "+esc(x.apartment):"")+'</small><small>'+date+'</small><small>'+esc(x.reliability_note||"")+'</small>'+(url?'<small><a href="'+esc(url)+'" target="_blank" rel="noopener noreferrer">Источник ↗</a></small>':"")+'</div>'}
function linked(label,url){let target=safeUrl(url);return target?'<a href="'+esc(target)+'" target="_blank" rel="noopener noreferrer">'+esc(label)+'</a>':""}
function photoInfo(p){let url=safeUrl(p.photo_url),src=safeUrl(p.photo_source_url),license=safeUrl(p.photo_license_url);return (url?'<img class="figure-thumb" loading="lazy" src="'+esc(url)+'" alt="Фотография: '+esc(p.name)+'">':"")+
'<p class="byline">'+esc(p.photo_author||"Автор неизвестен")+' · '+esc(p.photo_license||"лицензия уточняется")+'</p>'+
(src?'<p>'+linked("Открыть исходную фотографию ↗",src)+'</p>':"")+
(license?'<p>'+linked("Условия лицензии ↗",license)+'</p>':"")+
(p.preview_note?'<p class="byline">'+esc(p.preview_note)+'</p>':"")}
function cardHtml(f){const p=displayData(f.properties),[lon,lat]=f.geometry.coordinates;
const people=state.people.filter(x=>x.place_id===p.id);
const detailItems=(p.details||[]).map(x=>'<li>'+esc(x.text)+(x.status==="LEGEND"?' <span class="status-chip">Легенда</span>':x.status==="INTERPRETATION"?' <span class="status-chip">Интерпретация</span>':"")+'</li>').join("");
const knownSources=(p.sources||[]).map(s=>linked(s.title,s.url)).filter(Boolean).join("");
const extras=(p.external_links||[]).map(l=>linked(l.label,l.url)).filter(Boolean).join("");
const image=safeUrl(p.photo_url);
return '<div class="photo-cover">'+(image?'<img src="'+esc(image)+'" alt="'+esc(p.name)+'" loading="eager">':'<div class="no-photo">Фотография пока не выбрана</div>')+
'<button type="button" class="close-detail" id="close-detail" aria-label="Закрыть карточку">×</button></div>'+
'<div class="detail-body"><span class="pretitle">'+esc(p.category)+' · '+esc(p.id)+'</span><h2>'+esc(p.name)+'</h2><div class="address">⌖ '+esc(p.address||"Адрес уточняется")+'</div>'+
'<p class="lead">'+esc(p.why||p.description||"Историческое место")+'</p><div class="section-label">Открыть подробнее</div>'+
'<details name="place-content"><summary><span class="summary-icon">⌂</span>История и детали<span class="arrow">⌄</span></summary><div class="section-content"><p>'+esc(p.description||"Описание готовится")+'</p><p><strong>Что заметить:</strong> '+esc(p.look||"")+'</p>'+(detailItems?'<ul>'+detailItems+'</ul>':"")+'<p><strong>Доступ:</strong> '+esc(p.access_note||"Не подтверждён")+'</p></div></details>'+
'<details name="place-content"><summary><span class="summary-icon">♧</span>Люди и адреса <span class="status-chip">'+people.length+'</span><span class="arrow">⌄</span></summary><div class="section-content"><p class="byline">Исследовательские утверждения: первичные архивные свидетельства ещё требуют проверки. Владение не означает проживание.</p>'+(people.length?people.map(personMarkup).join(""):'<p>Связи пока не собраны</p>')+'</div></details>'+
'<details name="place-content"><summary><span class="summary-icon">▧</span>Фото и источники<span class="arrow">⌄</span></summary><div class="section-content">'+photoInfo(p)+'<div class="source-list">'+knownSources+extras+'</div>'+
(p.historic_photo_source_url?'<p class="byline">Исторический снимок: '+linked("открыть источник",p.historic_photo_source_url)+' (права требуют отдельной проверки)</p>':"")+'</div></details>'+
'<div class="card-actions"><a href="https://www.google.com/maps/dir/?api=1&travelmode=walking&destination='+lat+','+lon+'" target="_blank" rel="noopener noreferrer">Маршрут ↗</a><button id="share-place" type="button">Поделиться местом</button></div>'+
'<div class="card-footer">Пилот карты. Проверка допуска во дворы и достоверности отдельных исторических сведений ещё продолжается.</div></div>'}
function selectPlace(feature,move=true){state.selected=feature.properties.id;const card=q("#detail");card.innerHTML=cardHtml(feature);card.hidden=false;card.scrollTop=0;q("#close-detail").onclick=()=>{card.hidden=true;state.selected=null;renderAll()};q("#share-place").onclick=async()=>{const u=new URL(window.location.href);u.searchParams.set("place",state.selected);try{await navigator.clipboard.writeText(u.href);q("#share-place").textContent="Ссылка скопирована"}catch{window.prompt("Скопируйте ссылку:",u.href)}};markUrl(feature);setSearchOpen(false);renderAll();if(move){const [lon,lat]=feature.geometry.coordinates;map.flyTo({center:[lon,lat],zoom:15.25,duration:550})}}
function setSearchOpen(open){q("#search-toggle").setAttribute("aria-expanded",String(open));q("#search-drawer").hidden=!open;if(open)q("#search").focus()}
q("#search-toggle").onclick=()=>setSearchOpen(q("#search-drawer").hidden);
document.addEventListener("keydown",event=>{if(event.key==="Escape"){if(!q("#search-drawer").hidden)setSearchOpen(false);else if(!q("#detail").hidden)q("#close-detail").click()}});
Promise.all([
fetch("./data/places.geojson").then(r=>{if(!r.ok)throw Error("Не удалось получить места ("+r.status+")");return r.json()}),
fetch("./data/pilot-history.json").then(r=>r.ok?r.json():{records:[]}).catch(()=>({records:[]}))
]).then(([places,people])=>{state.features=places.features||[];state.people=people.records||[];const cats=["Все",...new Set(state.features.map(f=>f.properties.category))];const filters=q("#filters");for(const cat of cats){const button=document.createElement("button");button.textContent=cat;button.type="button";button.className=cat===state.filter?"active":"";button.onclick=()=>{state.filter=cat;filters.querySelectorAll("button").forEach(b=>b.classList.toggle("active",b===button));renderAll()};filters.append(button)}
q("#search").oninput=e=>{state.query=e.target.value.toLocaleLowerCase("ru");renderAll()};renderAll();
const id=new URLSearchParams(window.location.search).get("place");const initial=state.features.find(f=>f.properties.id===id);
if(initial)selectPlace(initial,false);
}).catch(error=>{setSearchOpen(true);q("#results-list").textContent="Ошибка загрузки данных: "+error.message});
