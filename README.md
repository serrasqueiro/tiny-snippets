# tiny-snippets
Set of submodules that are tiny snippets,
- [github tiny-snippets](https://github.com/serrasqueiro/tiny-snippets)

## Introduction

This module contains a set of basic snippets, originally from _**gist**_.
When reaching here, do:
- `git submodule update --init --recursive`
- or, just update your local repository if you did already download this repo:
  + `git submodule foreach "(git checkout master; git pull; echo ___)"`
To checkout locally to master, use:
  + `git submodule foreach "(git remote -v | sed s'/.*[\t]/FROM: /'; git checkout master; echo ^+++)"`

## Log history

Original [github](https://github.com/) repo [here](https://github.com/serrasqueiro/tiny-snippets/).

Bigger submodule(s):
1. [misc/keepit](https://github.com/serrasqueiro/keepit),
   + `git submodule add ../keepit.git misc/keepit`

Here are the list of historical adds.
1. [snippets/gist url](https://gist.github.com/serrasqueiro/08c51698a7668abba4ed6910f9a16ce3),
   + `git submodule add git@gist.github.com:08c51698a7668abba4ed6910f9a16ce3.git snippets/gist_url`
1. [snippets/git packers](https://gist.github.com/serrasqueiro/3b5705682767e04a4b4516da500c0930),
   + `git submodule add git@gist.github.com:3b5705682767e04a4b4516da500c0930.git snippets/git_packers`
1. [snippets/iban pt nib](https://gist.github.com/serrasqueiro/ed970d4306d6e824d29a9e9e136be654),
   + `git submodule add git@gist.github.com:ed970d4306d6e824d29a9e9e136be654.git snippets/iban_pt_nib`
1. [snippets/vias-principais](https://www.github.com/serrasqueiro/viasprincipais),
   + `git submodule add ../viasprincipais.git snippets/vias-principais`
1. [snippets/reident](https://gist.github.com/serrasqueiro/31e19db1dba146e512e4ea39c2c76279),
   + `git submodule add git@gist.github.com:31e19db1dba146e512e4ea39c2c76279.git snippets/reident`
1. [snippets/fastexcel](https://gist.github.com/serrasqueiro/fa9188a3fe219ef3e72371a00c633192),
   + `git submodule add git@gist.github.com:fa9188a3fe219ef3e72371a00c633192.git snippets/fastexcel`
1. [snippets/grelha-meo](https://gist.github.com/serrasqueiro/4537fea8688ee2712171dd71c5684079),
   + `git submodule add git@gist.github.com:4537fea8688ee2712171dd71c5684079.git snippets/grelha-meo`
1. [snippets/simple pop list](https://gist.github.com/serrasqueiro/5f5d9595b0b4020bdf1f337734f4c5a6),
   + `git submodule add git@gist.github.com:5f5d9595b0b4020bdf1f337734f4c5a6.git snippets/simple_pop_list`
1. [snippets/secs text](https://gist.github.com/serrasqueiro/c32c1579ad163d8c5c7f34eda28b208d),
   + `git submodule add git@gist.github.com:c32c1579ad163d8c5c7f34eda28b208d.git snippets/secs_text`
1. [snippets/states hash](https://gist.github.com/serrasqueiro/4de2939130d187e1b44965298c56d6c7),
   + `git submodule add git@gist.github.com:4de2939130d187e1b44965298c56d6c7.git snippets/states_hash`
1. [snippets/ls colors](https://gist.github.com/serrasqueiro/3cc4239e666baa4d8499cede47fc1f65),
   + `git submodule add git@gist.github.com:3cc4239e666baa4d8499cede47fc1f65.git snippets/ls_colors`
1. [snippets/ux colors](https://gist.github.com/serrasqueiro/717a2868b55275925784f9b3e874bcfe),
   + `git submodule add git@gist.github.com:717a2868b55275925784f9b3e874bcfe.git snippets/ux_colors`
1. [snippets/sampledates](https://gist.github.com/serrasqueiro/5c1a96781b401473025448c8473bd6f5),
   + `git submodule add git@gist.github.com:5c1a96781b401473025448c8473bd6f5.git snippets/sampledates`
1. [snippets/slb dates](https://github.com/serrasqueiro/jogaemcasa),
   + `git submodule add ../jogaemcasa.git snippets/slb_dates`
   + tiny-url 2022: [here](https://tinyurl.com/benfica2022), 2021 [here](https://gist.github.com/serrasqueiro/00aa98ed3a54f348fd5afdee81d8da6f/90d740575193c494d145e6c222627066705ba0e2)
1. [snippets/from java cc map](https://gist.github.com/serrasqueiro/2067e139bab4ed177c145921df28ba03)
   + `git submodule add git@gist.github.com:2067e139bab4ed177c145921df28ba03.git snippets/from_java_cc_map`
1. [snippets/country calling codes](https://gist.github.com/serrasqueiro/0bafc120f8e622a221e01f4b5221c718),
   + `git submodule add git@gist.github.com:0bafc120f8e622a221e01f4b5221c718.git snippets/country_calling_codes`
1. [snippets/url timeanddate](https://gist.github.com/serrasqueiro/70d2f1e4b149ef9fc6701ae7474e9d71),
   + `git submodule add git@gist.github.com:70d2f1e4b149ef9fc6701ae7474e9d71.git snippets/url_timeanddate`
1. [snippets/kitty](https://gist.github.com/serrasqueiro/0e4146eb59fe1cdfdd91477faf28747c),
   + `git submodule add git@gist.github.com:0e4146eb59fe1cdfdd91477faf28747c.git snippets/kitty`
1. [snippets/vboxsf mounting workaround](https://gist.github.com/serrasqueiro/d14e1805947a61d81e72a117b22aedeb),
   + `git submodule add git@gist.github.com:d14e1805947a61d81e72a117b22aedeb.git snippets/vboxsf_mounting_workaround`
1. [snippets/risco](https://gist.github.com/serrasqueiro/bb5c87a0d45947d056e7c1e0f05e9852),
   + `git submodule add git@gist.github.com:bb5c87a0d45947d056e7c1e0f05e9852.git snippets/risco`
1. [snippets/scrabble pt](https://gist.github.com/serrasqueiro/f816a81f15be86e7f4e49e1a99bd8424),
   + `git submodule add git@gist.github.com:f816a81f15be86e7f4e49e1a99bd8424.git snippets/scrabble_pt`
1. [snippets/meogonicks](https://gist.github.com/serrasqueiro/2aa675bf3deb13e5463554ac39b8fccd),
   + `git submodule add git@gist.github.com:2aa675bf3deb13e5463554ac39b8fccd.git snippets/meogonicks`
1. [snippets/meogonicks-info](https://gist.github.com/serrasqueiro/5aeb458f66e7499e76f7de1443df482f),
   + `git submodule add git@gist.github.com:5aeb458f66e7499e76f7de1443df482f.git snippets/meogonicks-info`
1. [snippets/dateformats](https://gist.github.com/serrasqueiro/94271c78dd6873fb5d0ad97d28806614),
   + `git submodule add git@gist.github.com:94271c78dd6873fb5d0ad97d28806614.git snippets/dateformats`
1. [snippets/git svnst](https://gist.github.com/serrasqueiro/b9591fac25f741b87c8560de5153457b),
   + `git submodule add git@gist.github.com:b9591fac25f741b87c8560de5153457b.git snippets/git_svnst`
1. [snippets/asciis](https://gist.github.com/serrasqueiro/0714e9d04039e5c29dedc60a1bd57f6e),
   + `git submodule add git@gist.github.com:0714e9d04039e5c29dedc60a1bd57f6e.git snippets/asciis`
1. [snippets/timeanddate calendars](https://gist.github.com/serrasqueiro/c634bade7d0fd53a4ccdf016bad0c3e2),
   + `git submodule add git@gist.github.com:c634bade7d0fd53a4ccdf016bad0c3e2.git snippets/timeanddate_calendars`
1. [snippets/farmacias](https://gist.github.com/serrasqueiro/4d4a36d4cf53ddb5987fb9607b6ceee5),
   + `git submodule add git@gist.github.com:4d4a36d4cf53ddb5987fb9607b6ceee5.git snippets/farmacias`
1. [snippets/curiosity](https://gist.github.com/serrasqueiro/f55bb4a18dabaabd82f05d3b2a3b8f24),
   + `git submodule add git@gist.github.com:f55bb4a18dabaabd82f05d3b2a3b8f24.git snippets/curiosity`
1. [snippets/links](https://gist.github.com/serrasqueiro/e9a6299636e40ca20c370b26c4b17830),
   + `git submodule add git@gist.github.com:e9a6299636e40ca20c370b26c4b17830.git snippets/links`
1. [snippets/local networks](https://gist.github.com/serrasqueiro/7d5781c554f163112ca8910e7b6b1fc9),
   + `git submodule add git@gist.github.com:7d5781c554f163112ca8910e7b6b1fc9.git snippets/local_networks`
1. [snippets/periodic table](https://gist.github.com/serrasqueiro/5a54eb09d36611ac45610460182d6451),
   + `git submodule add git@gist.github.com:5a54eb09d36611ac45610460182d6451.git snippets/periodic_table`
1. [snippets/python real](https://gist.github.com/serrasqueiro/bb335f02558d405cc893483e92571dab),
   + `git submodule add git@gist.github.com:bb335f02558d405cc893483e92571dab.git snippets/python_real`
1. [snippets/lista recibos](https://gist.github.com/serrasqueiro/8e0d3c59dd09f1485272ca5607c72a42),
   + `git submodule add git@gist.github.com:8e0d3c59dd09f1485272ca5607c72a42.git snippets/lista_recibos`
1. [snippets/arts](https://gist.github.com/serrasqueiro/f00b3ebc9f455a2bdb123a738b117b0c),
   + `git submodule add git@gist.github.com:f00b3ebc9f455a2bdb123a738b117b0c.git snippets/arts`
1. [snippets/lambda howto](https://gist.github.com/serrasqueiro/7fe2d7c44a321933fdca36abd6c991f9),
   + `git submodule add git@gist.github.com:7fe2d7c44a321933fdca36abd6c991f9.git snippets/lambda_howto`
1. [snippets/dice art](https://gist.github.com/serrasqueiro/234642475cc617dbaec10c69ad12b159),
   + `git submodule add git@gist.github.com:234642475cc617dbaec10c69ad12b159.git snippets/dice_art`
1. [snippets/iban howto](https://gist.github.com/serrasqueiro/771d58360164b224122ea62cc577518b),
   + `git submodule add git@gist.github.com:771d58360164b224122ea62cc577518b.git snippets/iban_howto`
1. [snippets/pub nipc](https://gist.github.com/serrasqueiro/1553a7f844d0d776e41a1c4da1f44611),
   + `git submodule add git@gist.github.com:1553a7f844d0d776e41a1c4da1f44611.git snippets/pub_nipc`
1. [snippets/gitouch](https://gist.github.com/serrasqueiro/9ab37fc6b58cc331f681f9959e16ef77),
   + `git submodule add git@gist.github.com:9ab37fc6b58cc331f681f9959e16ef77.git snippets/gitouch`
1. [snippets/nibans](https://gist.github.com/serrasqueiro/d58f203bd3a11eead463605e8182c589),
   + `git submodule add git@gist.github.com:d58f203bd3a11eead463605e8182c589.git snippets/nibans`
1. [snippets/deezing](https://gist.github.com/serrasqueiro/46290b9552a8d401ebe4b7921fee1a1a),
   + `git submodule add git@gist.github.com:46290b9552a8d401ebe4b7921fee1a1a.git snippets/deezing`
1. [snippets/alias git](https://gist.github.com/serrasqueiro/39ba0f48364b734cb9bd4637301306c2),
   + `git submodule add git@gist.github.com:39ba0f48364b734cb9bd4637301306c2.git snippets/alias_git`
1. [snippets/iban details](https://gist.github.com/serrasqueiro/00d7e8332b37f8eb9d5edb162eebc0ed),
   + `git submodule add git@gist.github.com:00d7e8332b37f8eb9d5edb162eebc0ed.git snippets/iban_details`
1. [snippets/roupanova](https://gist.github.com/serrasqueiro/22ef54cf198c00babd6d8f674cf0050f),
   + `git submodule add git@gist.github.com:22ef54cf198c00babd6d8f674cf0050f.git snippets/roupanova`
1. [snippets/yes](https://gist.github.com/serrasqueiro/0aec7e59bd94378632edbe13478da84c),
   + `git submodule add git@gist.github.com:0aec7e59bd94378632edbe13478da84c.git snippets/yes`
1. [snippets/portadosfundos](https://gist.github.com/serrasqueiro/ac2babe15767110edce5c9c74caa23e0),
   + `git submodule add git@gist.github.com:ac2babe15767110edce5c9c74caa23e0.git snippets/portadosfundos`
1. [snippets/rsspt](https://gist.github.com/serrasqueiro/da99deaa62e43d276e31f790b3095566),
   + `git submodule add git@gist.github.com:da99deaa62e43d276e31f790b3095566.git snippets/rsspt`
1. [snippets/geek ohqmoc](https://gist.github.com/serrasqueiro/f2ff63c3e3e7c5ab96f115d2ea561f31),
   + `git submodule add git@gist.github.com:f2ff63c3e3e7c5ab96f115d2ea561f31.git snippets/geek_ohqmoc`
1. [snippets/hmovies](https://gist.github.com/serrasqueiro/3f936c8bf99522738218ed6a70476b90),
   + `git submodule add git@gist.github.com:3f936c8bf99522738218ed6a70476b90.git snippets/hmovies`
1. [snippets/iso3166-1](https://gist.github.com/serrasqueiro/165c1f3659f56d5cbedbd90cf5b662c7),
   + `git submodule add git@gist.github.com:165c1f3659f56d5cbedbd90cf5b662c7.git snippets/iso3166-1`
1. [snippets/simple csv dump](https://gist.github.com/serrasqueiro/09633e4336c067b57e18dc815778ccde),
   + `git submodule add git@gist.github.com:09633e4336c067b57e18dc815778ccde.git snippets/simple_csv_dump`
1. [snippets/howtovdi](https://gist.github.com/serrasqueiro/566c98dd83a90eb12987dd896aea1902),
   + `git submodule add git@gist.github.com:566c98dd83a90eb12987dd896aea1902.git snippets/howtovdi`
1. [snippets/iuc](https://gist.github.com/serrasqueiro/6258d2f50c769179a32cd690dcea6aca),
   + `git submodule add git@gist.github.com:6258d2f50c769179a32cd690dcea6aca.git snippets/iuc`
1. [snippets/gitish](https://gist.github.com/serrasqueiro/1e491d1225947294fbe83e1827bee3b7),
   + `git submodule add git@gist.github.com:1e491d1225947294fbe83e1827bee3b7.git snippets/gitish`
1. [snippets/arts-dz](https://gist.github.com/serrasqueiro/4e1a5c961d3fbc2498969121e46caad1),
   + `git submodule add git@gist.github.com:4e1a5c961d3fbc2498969121e46caad1.git snippets/arts-dz`
1. [snippets/poker-dados](https://gist.github.com/serrasqueiro/0eda59f48e1df52c6d7d9cfe0dc029aa),
   + `git submodule add git@gist.github.com:0eda59f48e1df52c6d7d9cfe0dc029aa.git snippets/poker-dados`
1. [snippets/markdown doc](https://gist.github.com/serrasqueiro/2acb91a4c21ba5f46c64dc6c539093dc),
   + `git submodule add git@gist.github.com:2acb91a4c21ba5f46c64dc6c539093dc.git snippets/markdown_doc`
1. [snippets/bigfile](https://gist.github.com/serrasqueiro/86298610248e134a6c78dd4027ebc812),
   + `git submodule add git@gist.github.com:86298610248e134a6c78dd4027ebc812.git snippets/bigfile`
1. [snippets/adhoc](https://gist.github.com/serrasqueiro/aafdcbc01d1270acdf108c4e0aa2637e),
   + `git submodule add git@gist.github.com:aafdcbc01d1270acdf108c4e0aa2637e.git snippets/adhoc`
1. [snippets/racas](https://gist.github.com/serrasqueiro/c25376bf8480e3158b3fbb065e4ea529),
   + `git submodule add git@gist.github.com:c25376bf8480e3158b3fbb065e4ea529.git snippets/racas`
1. [snippets/beautifulsoup4-timestamps](https://gist.github.com/serrasqueiro/935a59a74fd8d743f5fa356d314a957b),
   + `git submodule add git@gist.github.com:935a59a74fd8d743f5fa356d314a957b.git snippets/beautifulsoup4-timestamps`
1. [snippets/fraudes](https://gist.github.com/serrasqueiro/f7a050a5f7c7b86e048f9e15b37c1953),
   + `git submodule add git@gist.github.com:f7a050a5f7c7b86e048f9e15b37c1953.git snippets/fraudes`
1. [snippets/tracing](https://gist.github.com/serrasqueiro/a7759461db40b52cadbcd141d6eff4cb),
   + `git submodule add git@gist.github.com:a7759461db40b52cadbcd141d6eff4cb.git snippets/tracing`
1. [snippets/tracing-examples](https://gist.github.com/serrasqueiro/16ee46eb0aea6aaeb2bcf5ec2538721e),
   + `git submodule add git@gist.github.com:16ee46eb0aea6aaeb2bcf5ec2538721e.git snippets/tracing-examples`
1. [snippets/am i](https://gist.github.com/serrasqueiro/7fd1d648363ba3c0e872be7f123b06c2),
   + `git submodule add git@gist.github.com:7fd1d648363ba3c0e872be7f123b06c2.git snippets/am_i`
1. [snippets/flashscore](https://gist.github.com/serrasqueiro/988c5fcf5045530d857419fc62d85ba4),
   + `git submodule add git@gist.github.com:988c5fcf5045530d857419fc62d85ba4.git snippets/flashscore`
1. [snippets/yes kudos](https://gist.github.com/serrasqueiro/8edfeef5b32a5e5195d78d9fce035438),
   + `git submodule add git@gist.github.com:8edfeef5b32a5e5195d78d9fce035438.git snippets/yes_kudos`
1. [snippets/whataboutfun](https://gist.github.com/serrasqueiro/c5a72c0cf73c64f7ec445d5c9e88bc44),
   + `git submodule add git@gist.github.com:c5a72c0cf73c64f7ec445d5c9e88bc44.git snippets/whataboutfun`
1. [snippets/youtube channels](https://gist.github.com/serrasqueiro/bf7faed2e78ca85808da025ea4bc1635),
   + `git submodule add git@gist.github.com:bf7faed2e78ca85808da025ea4bc1635.git snippets/youtube_channels`
1. [snippets/mundial2022](https://gist.github.com/serrasqueiro/b93cea0028c9f74eeea22ceb9259589d),
   + `git submodule add git@gist.github.com:b93cea0028c9f74eeea22ceb9259589d.git snippets/mundial2022`
1. [snippets/grelhas-prog](https://gist.github.com/serrasqueiro/69c94c48c3a78f4597266037b62d242e),
   + `git submodule add git@gist.github.com:69c94c48c3a78f4597266037b62d242e.git snippets/grelhas-prog`
1. [src/listers](https://gist.github.com/serrasqueiro/b3b2ecbdb2a4e9b3632c22483e72bbbe),
   + `git submodule add git@gist.github.com:b3b2ecbdb2a4e9b3632c22483e72bbbe.git src/listers`
1. [snippets/condos](https://gist.github.com/serrasqueiro/adee27ec209e97b6cf6b82eec6603e6c),
   + `git submodule add git@gist.github.com:adee27ec209e97b6cf6b82eec6603e6c.git snippets/condos`
1. [snippets/funds](https://gist.github.com/serrasqueiro/1b90d20a95c4c50b06aa7c24e116970e),
   + `git submodule add git@gist.github.com:1b90d20a95c4c50b06aa7c24e116970e.git snippets/funds`
1. [snippets/memorable](https://gist.github.com/serrasqueiro/0fac561e8819430c24343b30d030ddae),
   + `git submodule add git@gist.github.com:0fac561e8819430c24343b30d030ddae.git snippets/memorable`
1. [snippets/cmd](https://gist.github.com/serrasqueiro/b9cd37a5d5dc93a4b882164993bf5c23),
   + `git submodule add git@gist.github.com:b9cd37a5d5dc93a4b882164993bf5c23.git snippets/cmd`
1. [snippets/periodic-table](https://gist.github.com/serrasqueiro/dce730c265ccc0e9881eba5374a97f62),
   + `git submodule add git@gist.github.com:dce730c265ccc0e9881eba5374a97f62.git snippets/periodic-table`
1. [src/etc/piban](https://www.github.com/serrasqueiro/piban),
   + `git submodule add ../piban.git src/etc/piban`
1. [snippets/greader](https://gist.github.com/serrasqueiro/a312dc6e32a1841d6d50a4a31b93e963),
   + `git submodule add git@gist.github.com:a312dc6e32a1841d6d50a4a31b93e963.git snippets/greader`
1. [snippets/eredes](https://www.github.com/serrasqueiro/eredes),
   + `git submodule add ../eredes.git snippets/eredes`
1. [snippets/entidades-mb](https://gist.github.com/serrasqueiro/67649b0eb1914998dba4ab69dddd3a9d),
   + `git submodule add git@gist.github.com:67649b0eb1914998dba4ab69dddd3a9d.git snippets/entidades-mb`
1. [snippets/entidades-md](https://gist.github.com/serrasqueiro/86c6c26e31509a0e054bca8965b100e7),
   + `git submodule add git@gist.github.com:86c6c26e31509a0e054bca8965b100e7.git snippets/entidades-md`
1. [snippets/preferred-ssh](https://gist.github.com/serrasqueiro/cb87ffe0445bfe108dbd8d4ed73ab484),
   + `git submodule add git@gist.github.com:cb87ffe0445bfe108dbd8d4ed73ab484.git snippets/preferred-ssh`

1. [snippets/risk](https://gist.github.com/serrasqueiro/7011cdf094746f44bf3be47d4f8bcfd4),
   + `git submodule add git@gist.github.com:7011cdf094746f44bf3be47d4f8bcfd4.git snippets/risk`
1. [snippets/debian minimal](https://www.github.com/serrasqueiro/debmin),
   + `git submodule add ../debmin.git snippets/debian_minimal`
1. [snippets/poker-videos](https://gist.github.com/serrasqueiro/3b885690f901cefd7e585ae56bfe535d),
   + `git submodule add git@gist.github.com:3b885690f901cefd7e585ae56bfe535d.git snippets/poker-videos`
1. [snippets/bimbos](https://gist.github.com/serrasqueiro/263b0bfab436cffa34725b58f07c2a67),
   + `git submodule add git@gist.github.com:263b0bfab436cffa34725b58f07c2a67.git snippets/bimbos`
1. [snippets/porteiros](https://gist.github.com/serrasqueiro/13e0ccdf84bf98b4777a47c62c674da1),
   + `git submodule add git@gist.github.com:13e0ccdf84bf98b4777a47c62c674da1.git snippets/porteiros`
1. [snippets/cvs-howto](https://gist.github.com/serrasqueiro/c56d395bd85eea0815dfaea48e1106cd),
   + `git submodule add git@gist.github.com:c56d395bd85eea0815dfaea48e1106cd.git snippets/cvs-howto`
1. [snippets/lff](https://gist.github.com/serrasqueiro/a02c36a90c1d2e6f2139f522349507a1),
   + `git submodule add git@gist.github.com:a02c36a90c1d2e6f2139f522349507a1.git snippets/lff`
1. [snippets/netflixdude](https://gist.github.com/serrasqueiro/6361b35fc1882f43a60dca63a9443d08),
   + `git submodule add git@gist.github.com:6361b35fc1882f43a60dca63a9443d08.git snippets/netflixdude`
1. [snippets/video-porteiro](https://gist.github.com/serrasqueiro/15705e50326c1abebf9f7608a1d01e40),
   + `git submodule add git@gist.github.com:15705e50326c1abebf9f7608a1d01e40.git snippets/video-porteiro`
1. [snippets/consignar-irs](https://gist.github.com/serrasqueiro/09cd7b7e35d4d13a6289c0c2afc836c5),
   + `git submodule add git@gist.github.com:09cd7b7e35d4d13a6289c0c2afc836c5.git snippets/consignar-irs`
1. [snippets/ikea](https://gist.github.com/serrasqueiro/6a584b95af1f593eb9480853f52fefc1),
   + `git submodule add git@gist.github.com:6a584b95af1f593eb9480853f52fefc1.git snippets/ikea`
1. [snippets/caes-segurados](https://gist.github.com/serrasqueiro/eb4ed1262be49d2442cec7130e2c9fbb),
   + `git submodule add git@gist.github.com:eb4ed1262be49d2442cec7130e2c9fbb.git snippets/caes-segurados`
1. [snippets/eurovision](https://gist.github.com/serrasqueiro/f69c3294dfc8b9129c95a7c474b212ac),
   + `git submodule add git@gist.github.com:f69c3294dfc8b9129c95a7c474b212ac.git snippets/eurovision`
1. [snippets/shakira](https://gist.github.com/serrasqueiro/2581967589f17db3747cd07c4ae2081e),
   + `git submodule add git@gist.github.com:2581967589f17db3747cd07c4ae2081e.git snippets/shakira`
1. [snippets/colores](https://gist.github.com/serrasqueiro/68148115a7b67a1537ca8d057815af17),
   + `git submodule add git@gist.github.com:68148115a7b67a1537ca8d057815af17.git snippets/colores`
1. [snippets/vpt-samples](https://gist.github.com/serrasqueiro/cbccc8bfeae59dae14afeadaf07617d7),
   + `git submodule add git@gist.github.com:cbccc8bfeae59dae14afeadaf07617d7.git snippets/vpt-samples`
1. [snippets/olhaogelado](https://www.github.com/serrasqueiro/olhaogelado),
   + `git submodule add ../olhaogelado.git snippets/olhaogelado`
1. [snippets/another 4433185](https://gist.github.com/serrasqueiro/c22acb8c3044747bd083e9f720de23e7),
   + `git submodule add git@gist.github.com:c22acb8c3044747bd083e9f720de23e7.git snippets/another_4433185`
1. [snippets/greek-alphabet](https://gist.github.com/serrasqueiro/c8ff5a94328a346b722e825c471b200e),
   + `git submodule add git@gist.github.com:c8ff5a94328a346b722e825c471b200e.git snippets/greek-alphabet`
1. [snippets/wifi-routers](https://gist.github.com/serrasqueiro/1b6583049a21cd2a35c74a40eff73a6e),
   + `git submodule add git@gist.github.com:1b6583049a21cd2a35c74a40eff73a6e.git snippets/wifi-routers`
1. [snippets/vuplayer-cddb](https://gist.github.com/serrasqueiro/c4245e84072b63815f49ead5974f61ab),
   + `git submodule add git@gist.github.com:c4245e84072b63815f49ead5974f61ab.git snippets/vuplayer-cddb`
1. [snippets/youtubing](https://gist.github.com/serrasqueiro/4252c18f725f799136701503c50710b4),
   + `git submodule add git@gist.github.com:4252c18f725f799136701503c50710b4.git snippets/youtubing`
1. [snippets/dissertacao](https://gist.github.com/serrasqueiro/aa927bbc0a31e62c91d640e00c081887),
   + `git submodule add git@gist.github.com:aa927bbc0a31e62c91d640e00c081887.git snippets/dissertacao`
1. [snippets/dogs](https://gist.github.com/serrasqueiro/083ecd7fd6c823686595835d1a311894),
   + `git submodule add git@gist.github.com:083ecd7fd6c823686595835d1a311894.git snippets/dogs`
1. [snippets/filefly](https://gist.github.com/serrasqueiro/83346f41df6cb0c21cfdb92dd5dce3f0),
   + `git submodule add git@gist.github.com:83346f41df6cb0c21cfdb92dd5dce3f0.git snippets/filefly`
1. [snippets/dominant iban](https://gist.github.com/serrasqueiro/d3111c299e87ec814fc3c7c8b915c116),
   + `git submodule add git@gist.github.com:d3111c299e87ec814fc3c7c8b915c116.git snippets/dominant_iban`
1. [snippets/manual-esquentador](https://gist.github.com/serrasqueiro/247b51606d12bd14a4230a49f33133e1),
   + `git submodule add git@gist.github.com:247b51606d12bd14a4230a49f33133e1.git snippets/manual-esquentador`
1. [snippets/bancos-online](https://gist.github.com/serrasqueiro/249523b078d33dc8a78efd4caf95914c),
   + `git submodule add git@gist.github.com:249523b078d33dc8a78efd4caf95914c.git snippets/bancos-online`
1. [snippets/scanrec](https://gist.github.com/serrasqueiro/1dffa8ea30ad302a7c12eaaff741d17a),
   + `git submodule add git@gist.github.com:1dffa8ea30ad302a7c12eaaff741d17a.git snippets/scanrec`
1. [snippets/pizzas](https://gist.github.com/serrasqueiro/014ade48300aee68bad1c90167a84890),
   + `git submodule add git@gist.github.com:014ade48300aee68bad1c90167a84890.git snippets/pizzas`
1. [snippets/chave-movel-digital](https://gist.github.com/serrasqueiro/dbe088e2a86c532ac17eeeafaf2ab541),
   + `git submodule add git@gist.github.com:dbe088e2a86c532ac17eeeafaf2ab541.git snippets/chave-movel-digital`
1. [snippets/banco-ibans](https://gist.github.com/serrasqueiro/c2e1bc13959ec52f2f59b38593dd5ae1),
   + `git submodule add git@gist.github.com:c2e1bc13959ec52f2f59b38593dd5ae1.git snippets/banco-ibans`
1. [snippets/atestado-incapacidade](https://gist.github.com/serrasqueiro/3b59298acd56f5d836f2c7667a4c4390),
   + `git submodule add git@gist.github.com:3b59298acd56f5d836f2c7667a4c4390.git snippets/atestado-incapacidade`
1. [snippets/how-to-submodule](https://gist.github.com/serrasqueiro/3f1ff4f213a049afc624283aac7197fb),
   + `git submodule add git@gist.github.com:3f1ff4f213a049afc624283aac7197fb.git snippets/how-to-submodule`
1. [snippets/subnet](https://gist.github.com/serrasqueiro/79ed101f7aae014ead931ac60c778b50),
   + `git submodule add git@gist.github.com:79ed101f7aae014ead931ac60c778b50.git snippets/subnet`
1. [snippets/earth-view](https://gist.github.com/serrasqueiro/c887bcf4ffec9373267e38db459f7a50),
   + `git submodule add git@gist.github.com:c887bcf4ffec9373267e38db459f7a50.git snippets/earth-view`
1. [snippets/youtube-urls](https://gist.github.com/serrasqueiro/c2e1ed9dd300cc3bc2e27b76a34ce120),
   + `git submodule add git@gist.github.com:c2e1ed9dd300cc3bc2e27b76a34ce120.git snippets/youtube-urls`
1. [snippets/WEBP2JPG](https://www.github.com/serrasqueiro/WEBP2JPG),
   + `git submodule add ../WEBP2JPG.git snippets/WEBP2JPG`
1. [snippets/dir-lists](https://gist.github.com/serrasqueiro/ec9e4f55c3bb35b12d8b7cc14ca05b8a),
   + `git submodule add git@gist.github.com:ec9e4f55c3bb35b12d8b7cc14ca05b8a.git snippets/dir-lists`
1. [snippets/base32](https://gist.github.com/serrasqueiro/7e1fd27b8034e80f361cb149f264f6b1),
   + `git submodule add git@gist.github.com:7e1fd27b8034e80f361cb149f264f6b1.git snippets/base32`
1. [snippets/pangrama](https://gist.github.com/serrasqueiro/17e08b471628f568de2e34248c68e27c),
   + `git submodule add git@gist.github.com:17e08b471628f568de2e34248c68e27c.git snippets/pangrama`
1. [snippets/windows-atalhos](https://gist.github.com/serrasqueiro/75a422121b595f89408b76a7c9048bc2),
   + `git submodule add git@gist.github.com:75a422121b595f89408b76a7c9048bc2.git snippets/windows-atalhos`
1. [snippets/tiny-crc-32](https://gist.github.com/serrasqueiro/f2302adad195bcbcdd825ed9a6a2065c),
   + `git submodule add git@gist.github.com:f2302adad195bcbcdd825ed9a6a2065c.git snippets/tiny-crc-32`
1. [snippets/youtube-alpha](https://gist.github.com/serrasqueiro/f54f224114200f9964483981b6397000),
   + `git submodule add git@gist.github.com:f54f224114200f9964483981b6397000.git snippets/youtube-alpha`
1. [snippets/tempestades](https://gist.github.com/serrasqueiro/df9e8c1286e4c3ed78964ea9845ca843),
   + `git submodule add git@gist.github.com:df9e8c1286e4c3ed78964ea9845ca843.git snippets/tempestades`
1. [snippets/liga-portugal](https://gist.github.com/serrasqueiro/712669161699c4296b88d712019f1a80),
   + `git submodule add git@gist.github.com:712669161699c4296b88d712019f1a80.git snippets/liga-portugal`
1. [snippets/damn-after-local](https://gist.github.com/serrasqueiro/39f993cfffee68780842e76e01678533),
   + `git submodule add git@gist.github.com:39f993cfffee68780842e76e01678533.git snippets/damn-after-local`
1. [snippets/windows-tail](https://gist.github.com/serrasqueiro/da5fbad7916863a78b75f6a7023bc779),
   + `git submodule add git@gist.github.com:da5fbad7916863a78b75f6a7023bc779.git snippets/windows-tail`
1. [snippets/virtualbox-disks](https://gist.github.com/serrasqueiro/59bcae507f55602070fe9b3746710598),
   + `git submodule add git@gist.github.com:59bcae507f55602070fe9b3746710598.git snippets/virtualbox-disks`
1. [snippets/elegant-clock](https://gist.github.com/serrasqueiro/88d6576dc3860b19a39854e96b875ecc),
   + `git submodule add git@gist.github.com:88d6576dc3860b19a39854e96b875ecc.git snippets/elegant-clock`
1. [snippets/submodulecleaner](https://gist.github.com/serrasqueiro/3fff85f0fca07f36d7ead661aa6274a5),
   + `git submodule add git@gist.github.com:3fff85f0fca07f36d7ead661aa6274a5.git snippets/submodulecleaner`
1. [snippets/bash-alias](https://gist.github.com/serrasqueiro/4a268047eb5ffb4991ef0c4233aad552),
   + `git submodule add git@gist.github.com:4a268047eb5ffb4991ef0c4233aad552.git snippets/bash-alias`
