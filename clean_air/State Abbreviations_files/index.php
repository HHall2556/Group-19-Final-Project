window.googletag = window.googletag || {};
window.googletag.cmd = window.googletag.cmd || [];
(function (W, D, N) {
W[N]=W[N]||{};W[N].cmd=W[N].cmd||[];
function getDbg(){var dbg=0,m;try{m = W.location.href.match(/pbjs_debug=(\S*)/) || (D.cookie+';').match(/pbjs_debug=(\S*)\;/);dbg=m && 'true'===(m[1]||'')}catch(e){}D.cookie='pbjs_debug='+dbg+'; path=/; secure';return dbg}
W.G_options=W.G_options||{};
W.G_options.debug=getDbg();
var G_debug=G_options.debug;
function loadScript(url){var o='script',s=document,a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=url;m.parentNode.insertBefore(a,m);};

if(W[N]['affmp2_50states.com']){return}W[N]['affmp2_50states.com']=1;
loadScript('https://cdn4-hbs.affinitymatrix.com/hvrlib/50states.com/1615548025/v2.js');
W[N].cmd.push(function(){
if(!W[N].chkDomain('50states.com')){return}
var cfg = {"aff":{"def":{"maxCall":1,"minVisblePerc":50,"delaySec":30,"kw":{"domain":"50states.com"},"zads":{"enabled":true},"gads":{"enabled":true,"rmslot":0,"cmpsz":{"w_max_perc":2,"h_max_perc":2,"szMobileOnly":["320x50"]},"vspace":"middle","allowWoSlot":1},"dfpenblsrv":true},"aus":[{"au":"/42115163/IP_50states.com_ALL_Multisize_RON_Both_HVR","sz":["970x90","970x250","300x250","300x600","728x90","160x600"],"def":1},{"au":"/21930596546/IP_50states.com_ALL_Multisize_RON_Both_HVR_MC","sz":["970x90","970x250","300x250","300x600","728x90","160x600"],"def":1}]},"pub":{"def":{"maxCall":1,"delaySec":30,"minVisblePerc":50,"reprf":1,"msz":false,"kw":{"domain":"50states.com"},"excludePatrn":{"patrn":"NO_REFRESH","enable":1},"section":{"enable":0,"whitelist":[],"blacklist":[]}},"rule":[{"tp":"exc","au":["*"],"sz":["1x1"],"lbl":"Ignr 1x1"},{"tp":"inc","au":["*"],"sz":["970x90","970x250","300x250","300x600","728x90","160x600"],"lbl":"All Au"}],"adspots":[]}};
if(cfg.aff.pbjs && cfg.aff.pbjs.enabled){
    var hbsite = cfg.aff.pbjs.hbsite || ('hvr_' + cfg.aff.def.kw.domain),d=new Date();
    W[N].U.loadScript('https://hbs.ph.affinity.com/v5/' + hbsite + '/affhb.data.js.php?t=' + d.getDate() + d.getMonth() + d.getHours() );
}
if( cfg.aff.def.dfpenblsrv){W[N].U.loadScript("https://securepubads.g.doubleclick.net/tag/js/gpt.js");}
googletag.cmd.push(function() {
    W[N].AffRefresh(cfg)
});
});
})(window, document, '__afflib');