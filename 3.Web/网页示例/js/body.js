//获取元素
var box = document.getElementsByClassName("left1")[0];
var li11 = document.getElementsByClassName("li1");
function func(sum) {
    switch (sum){
        case 1:
            box.style.backgroundImage = "url('https://res.shiguangkey.com//file/201806/19/20180619142252602590185.jpg')";

            break;
        case 2:
            box.style.backgroundImage = "url('https://res.shiguangkey.com//file/201806/19/20180619141337485823895.jpg')";
            break;
        case 3:
            box.style.backgroundImage = "url('https://res.shiguangkey.com//file/201806/21/20180621150342030454625.jpg')";
            break;
        case 4:
            box.style.backgroundImage = "url('https://res.shiguangkey.com//file/201805/17/20180517113424433990524.jpg')";
            break;
    }
}
setInterval("right()",3000);

// 左右箭头的事件
var time = 1;
function right() {
    time += 1;
    if(time > 4){
        time = 1;
    }
    func(time);
}
function left() {
    time -= 1;
    if(time < 1){
        time = 4;
    }
    func(time);
}

// 圆圈的点击事件
li11[0].onclick = function () {
    func(1);
}
li11[1].onclick = function () {
    func(2);
}
li11[2].onclick = function () {
    func(3);
}
li11[3].onclick = function () {
    func(4);
}

//切换功能的事件
$(function () {
    $(".left3 li").click(function () {
        $(this).addClass("active").siblings().removeClass("active");
        var num = $(this).index();
        // console.log(num);
        var $li4 = $(".left4 li");
        $li4.eq(num).removeClass("hide").addClass("show");
        $li4.eq(num).siblings().removeClass("show").addClass("hide");
    });
});