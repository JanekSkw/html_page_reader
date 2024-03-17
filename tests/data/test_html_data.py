REF_HTML_1 = """
              <html>
                <head>
                    <title> tytul raz daw trzy </title>
                    <style>.call {background-color:black;} </style>
                    <script>1234
                    555
                    fghjjkkk</script>
                </head>
                <body>
                    jest
                    <div>Fajny tytul tytul tytul tytul</div>
                </body>
                raz raz
                dwa a g h. j:: htkl!@#$%
              </html>
            """


REF_HTML_2 = """
</body><script>
    window.addEventListener('SurvicateReady', function() {
        _sva.setVisitorTraits({ "BDsegpm": "empty" });
    });
    window.WP.push(function() {
        WP.gdpr.runAfterConsent(function() {
            WP.getScript({
                src: "https://survey.survicate.com/workspaces/a2d92acc5ba878813a1e6c0a0726fd85/web_surveys.js",
                target: document.body,
                id: "survicate-poll"
            })
        })
    })
    </script>a a a a a a a a a a  a aa  a aaaa  aaa      aaaa  aaaaaaa aa a </html>
"""

REF_HTML_3 = """
<style>dfp-gazetawyborcza #pageHead.hasBanner .c0{top:40px;position:absolute}</style><script class="optanon-category-C0004" type="text/plain" src="https://mrb.upapi.net/org?o=4829226047897600&upapi=true"></script>
<script>
dfpParams.video.preroll = '//pubads.g.doubleclick.net/gampad/ads?sz=400x300|640x480&iu=/75224259/AGORA-IN/GazetaHP/090-PREROLL&cust_params=pos%3D090-PREROLL%26dx%3D162835%26jsp%3D30%26dir%3DHP2018%26kw%3D[brandsafe]%26dystrybutor%3D[distributor_id]%26domena%3Dwww.gazeta.pl%26yb_ab%3D'+AdviewAdsTag._YB.ab()+'&url=[locationhref]&description_url=[locationhref]&impl=s&gdfp_req=1&env=vp&output=vast&unviewed_position_start=1&correlator=[timestamp]';
</script>
<script>
                if(AdviewAdsTag && AdviewAdsTag.kwTargeting && typeof AdviewAdsTag.kwTargeting === 'object'){
                    AdviewAdsTag.kwTargeting.push("dfp10");
                }
            </script>
            <!-- Using DFP provider 1.0 -->
        <script type="text/javascript">

                        var dfp_slot_000_mainboard;

                        var dfp_slot_071_winieta;

                        var dfp_slot_001_topboard;


        googletag.cmd.push(function() {
   </script>
"""