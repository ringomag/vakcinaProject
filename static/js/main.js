//var template = document.getElementsByClassName('za_tippy');
// console.log("lista",template);
// tippy('.btn-primary', {
  // content: template.innerHTML,
  // allowHTML: true,
// });

// const { javascript } = require("webpack")

// Problem u tvojoj realizaciji je to sto postoji vise templatea saa razlicitim sadrzajem. Izvukao si var template = document.getElementsByClassName('za_tippy');
// i to ti je lista span elemenata. Kada postavis to kao content i napises content: template.innerHTML, ti pokusavas da kao kontent postavis innerHtml LISTE a ne elementa.
// Prvo savet jedan: nemoj koristiti iste klase zaa CSS i za javascript. Zato sam u svojim resenjima dodao btn-tippy kao klasu koja ce mi sluziti samo za javascript.
// U slucaju da neko uzme da sredjuje CSS, moze da se desi da obrise neku klasu koja ti sluzi i za javascript.
// Dodao sam u html id="za_tippy-{{i.id}}" da bih mogao po ID-ju, jedinstveno da izvlacis template koji ti je potreban.
//  Da bi element na kome prevuces misa znao po kom ID-ju da trazi template dodao sam data-template="za_tippy-{{i.id}}".



// prvi nacin
// Ovo ti je iz dokumentacije :https://atomiks.github.io/tippyjs/v6/html-content/#template-linking
// Videces prvu recenicu: " If you have multiple references each with their own unique template, there is a way to link them with their associated template:".
// To ti je u stvari problem sa kojim si se ti susreo
// Posto ti je u javasccriptu sve funkcija, umesto da pises template.innerHTML, ti napravis funkciju koja ce po id-ju da nadje template i vrati njegov innerHTML.
// Namerno sam ti ostavio console.log ispod da vidis sta je po dukmentaciji ulaz u funkciju za vracanje contenta(element na koga si prevukao misa)



  tippy('.btn-tippy', {

    content(reference) {
      console.log('reference', reference);
      const id = reference.getAttribute('data-template');
      const template = document.getElementById(id);
      return template.innerHTML;
    },
    allowHTML: true,
    placement: 'left',
    theme: 'blue',
    animation: 'perspective',
  });

// drugi nacin
// Ovo je bez dokumentacije. Dodao sam ga na dugme Uredi i dodao sam klasu btn-tippy-2 da bi ih razlikovao.
//  Zasniva se resenje na tome da inicijalizujes svaki tootltip za svaki element posebno.
// Dakle prvo nadjemo elemente na kojima ce se prikazivati tooltip(kada se prevuce misem). To je let elements.
// Onda u for petlji prolazimo kroz te elemente i za svaki element nadjemo pripadajuci template po id-ju koji smo izvukli iz data-template.
// I posto imamo zaseban element i zaseban template inicijalizujemo tippy samo za taaj par.
// Ovo resenje je malo manje optimalno zbog for petlje ali je i vise nego legitimno i nece napraviti nikakvu razliku u perforamansama.
// var elements = document.getElementsByClassName('btn-tippy-2');
// for (i = 0; i < elements.length; i++) {
//   let element = elements[i];
//   let id = element.getAttribute('data-template');
//   let template = document.getElementById(id);
//   tippy(element, {
//     content: template.innerHTML,
//     allowHTML: true,
//   });
// }
var modals = document.getElementsByClassName('modal');
// Get the button that opens the modal
var btns = document.getElementsByClassName("openmodal");
var spans=document.getElementsByClassName("close");
for(let i=0;i<btns.length;i++){
    btns[i].onclick = function() {
        modals[i].style.display = "block";
    }
}
for(let i=0;i<spans.length;i++){
    spans[i].onclick = function() {
        modals[i].style.display = "none";
    }
}
