alert("You're on a Youtube page!")
var firstHref = $("a[href^='http']").eq(0).attr("href");
var secondhref = $("a[href^='http']").eq(1).attr("href");
console.log(firstHref);