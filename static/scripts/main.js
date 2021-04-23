const mobile_nav = document.getElementById('mob-nav');
const ham_btn = document.getElementById('ham_btn');
const menu_items = document.getElementsByClassName('menu-items')[0].children;
console.log(menu_items);

console.log(ham_btn);

ham_btn.addEventListener('click', ()=>{
    mobile_nav.classList.add('nav-active');
})

for(i=0;i<menu_items.length;i++){
    menu_items[i].addEventListener('click', ()=>{
        mobile_nav.classList.remove('nav-active');
    })
}

new Glide('.glide', {
    type: 'carousel',
    startAt: 0,
    autoplay:  2000
}).mount()