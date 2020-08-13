//启动项目
setTimeout(() => {
            document.getElementsByTagName("button")[0].click();
        }, 1000);
//判断有无
var sleeptime=3000
setInterval(() => {
    if (document.getElementsByClassName('ant-radio ant-radio-disabled')[0]!=null) {
        document.getElementsByTagName("button")[5].click();
        document.getElementsByTagName("button")[0].click();
    }
    else{
        document.getElementsByClassName('ant-radio-wrapper')[1].click();
        document.getElementsByTagName("button")[4].click();
        setTimeout(() => {
            var url=document.getElementsByClassName('ant-modal-footer')[0].innerHTML;
            var patt = new RegExp("https://(.*?).ipynb" );
            window.location.href=patt.exec(url)[0];
        }, 12000);
    }
  }, 1000)
  
