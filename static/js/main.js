var template = document.getElementsByClassName('za_tippy');
//for (var i = 0; i < template.length; i++) { }
console.log("lista",template);
  tippy('.btn-primary', {
    content: template.innerHTML,
    allowHTML: true,
  });
