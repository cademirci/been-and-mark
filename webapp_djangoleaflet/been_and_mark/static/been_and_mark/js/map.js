
// map can be initialized here also, I would prefer that, for a clean code but
// I could not find a way to use django template variables in a static file.
// I think I should use a regular frontend framework for it, however this is a
// small project. I left these for now.

window.addEventListener("map:init", function(e) {
    // var detail = e.detail;
    // L.marker([39.49079, 26.33685]).addTo(detail.map);
}, false);
