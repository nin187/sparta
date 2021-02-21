document.addEventListener("DOMContentLoaded", function () {
    let animals = ['ねずみ', 'うし', 'とら', 'うさぎ', 'たつ', 'へび', 'うま', 'ひつじ', 'さる', 'とり', 'いぬ', 'いのしし'];
    let animals2 = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'];
    let year = getParameter('year') == '' ? 1 : getParameter('year');
    let id_1 = `eto${year}_1`;
    let id_2 = `eto${year}_2`;
    let animal = animals[year - 1];
    let animal2 = animals2[year - 1];
    document.getElementById(id_1).style.display = 'block';
    document.getElementById(id_2).style.display = 'block';
    document.getElementsByClassName('eto')[0].innerHTML = animal;
    document.getElementsByClassName('eto')[0].style.backgroundImage = `url('yearS${year}.png')`;
    document.getElementsByTagName('h1')[0].innerHTML = `【2021年】${animal2}年生まれの全体運`;
    document.getElementById('sub_title1').textContent = `${animal2}年生まれの備え持った気質`;
    document.getElementById('sub_title2').textContent = `${animal2}年生まれの全体運`;
});

function getParameter(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}