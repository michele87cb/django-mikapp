/**
 * Created by michele on 04/06/16.
 */

window.onerror = function(msg, url, line, col, error) {
   // Note that col & error are new to the HTML 5 spec and may not be
   // supported in every browser.  It worked for me in Chrome.
   var extra = !col ? '' : '\ncolumn: ' + col;
   extra += !error ? '' : '\nerror: ' + error;

   // You can view the information in an alert to see things working like this:
   notify_show(msg,"error");

   var suppressErrorAlert = true;
   // If you return true, then error alerts (like in older versions of
   // Internet Explorer) will be suppressed.
   return suppressErrorAlert;
};

function navmenu_www(pyfunz){
    try{
        var content = $('#pageContent').load(pyfunz);
    }
    catch(e){
        alert_www('Errore di eccezione',e.message);
    }

}

function alert_www(title,message,funz){
    title = typeof title !== 'undefined' ? title : null;
    message = typeof message !== 'undefined' ? message : 'Messaggio non passato alla funzione';
    $.alert({
        title: title,
        content: message,
        theme: 'black'
    })
}

function notify_show(testo,tipo,position,delay){
    testo = typeof testo !== 'undefined' ? testo : "Messaggio non passato alla funzione";
    tipo = typeof tipo !== 'undefined' ? tipo : "info";
    position = typeof position !== 'undefined' ? position : "bottom left";
    delay = typeof delay !== 'undefined' ? delay : 5000;
    autoHide = true;
    if (delay == 0 || delay == false){
        autoHide = false
    }
    try{
        parseInt(delay);
    }
    catch(e){
        autoHide = false;
        delay = 5000;
    }
    $.notify(testo,{
        className: tipo,
        position: position,
        autoHideDelay : delay,
        autoHide : autoHide
    })
}

