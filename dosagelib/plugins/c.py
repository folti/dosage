# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..helpers import (
    _BasicScraper, constStarter, bounceStarter, indirectStarter)
from ..util import getQueryParams


class CalvinAndHobbes(_BasicScraper):
    latestUrl = 'http://www.gocomics.com/calvinandhobbes/'
    imageUrl = 'http://www.gocomics.com/calvinandhobbes/%s'
    imageSearch = compile(r'src="(http://picayune\.uclick\.com/comics/ch/[^"]+\.gif)"')
    prevSearch = compile(r'href="(.*?)"\s+onclick="[^"]*">Previous day</a>')
    help = 'Index format: yyyy/mm/dd'



class CandyCartoon(_BasicScraper):
    latestUrl = 'http://www.candycartoon.com/'
    imageUrl = 'http://www.candycartoon.com/archives/%s.html'
    imageSearch = compile(r'<img alt="[^"]*" src="(http://www\.candycartoon\.com/archives/[^"]+)"')
    prevSearch = compile(r'<a href="(http://www\.candycartoon\.com/archives/\d{6}\.html)">prev')
    help = 'Index format: nnnnnn'



class CaptainSNES(_BasicScraper):
    latestUrl = 'http://captainsnes.com/'
    imageUrl = 'http://captainsnes.com/?date=%s'
    imageSearch = compile(r'<img src=\'(http://www.captainsnes.com/comics/.+?)\'')
    prevSearch = compile(r'<a href="http://www.captainsnes.com/(.+?)"><span class="prev">')
    help = 'Index format: yyyymmdd'



class CaribbeanBlue(_BasicScraper):
    latestUrl = 'http://cblue.katbox.net/'
    imageUrl = 'http://cblue.katbox.net/index.php?strip_id=%s'
    imageSearch = compile(r'="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src="images/navigation_back.png"')
    help = 'Index format: n (unpadded)'



class Catena(_BasicScraper):
    latestUrl = 'http://catenamanor.com/'
    imageUrl = 'http://catenamanor.com/index.php?comic=%s'
    imageSearch = compile(r'(comics/catena/.+?)"')
    prevSearch = compile(r'First</a>.+?"(.+?)".+?Previous')
    help = 'Index format: n (unpadded)'


class Catharsis(_BasicScraper):
    latestUrl = 'http://catharsiscomic.com/'
    imageUrl = 'http://catharsiscomic.com/archive.php?strip=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+"Previous')
    help = 'Index format: yymmdd-<your guess>.html'



class ChasingTheSunset(_BasicScraper):
    latestUrl = 'http://www.fantasycomic.com/'
    imageUrl = 'http://www.fantasycomic.com/index.php?p=c%s'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'



class Chisuji(_BasicScraper):
    latestUrl = 'http://www.chisuji.com/'
    imageUrl = 'http://www.chisuji.com/%s'
    imageSearch = compile(r'<img src="(http://www.chisuji.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.chisuji.com/.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'



class ChugworthAcademy(_BasicScraper):
    latestUrl = 'http://chugworth.com/'
    imageUrl = 'http://chugworth.com/?p=%s'
    imageSearch = compile(r'<img src="(.+?)" alt="Comic')
    prevSearch = compile(r'<a href="(http://chugworth.com/\?p=\d{1,4})"[^>]+?title="Previous">')
    help = 'Index format: n (unpadded)'



class ChugworthAcademyArchive(_BasicScraper):
    latestUrl = 'http://chugworth.com/archive/?strip_id=422'
    imageUrl = 'http://chugworth.com/archive/?strip_id=%s'
    imageSearch = compile(r'<img src=(comics/\d+.+?.\w{1,4})')
    prevSearch = compile(r'<a href=\'(.+?)\'><img src=\'images/previous.gif')
    help = 'Index format: nnn'



class CigarroAndCerveja(_BasicScraper):
    latestUrl = 'http://www.cigarro.ca/'
    imageUrl = 'http://www.cigarro.ca/?p=%s'
    imageSearch = compile(r"(/comics/.+?)'")
    prevSearch = compile(r'(/\?p=.+?)">&laq')
    help = 'Index format: non'



class CombustibleOrange(_BasicScraper):
    latestUrl = 'http://www.combustibleorange.com/'
    imageUrl = 'http://www.combustibleorange.com/index.php?current=%s'
    imageSearch = compile(r'<img src="(/images/comics/\d+?\.gif)"')
    prevSearch = compile(r'><a href="(.+?)"><img src="images/button-last.gif" border="0">')
    help = 'Index format: n (unpadded)'



class Comedity(_BasicScraper):
    latestUrl = 'http://www.comedity.com/'
    imageUrl = 'http://www.comedity.com/index.php?strip_id=%s'
    imageSearch = compile(r'<img src="(Comedity_files/.+?)"')
    prevSearch = compile(r'<a href="(/?index.php\?strip_id=\d+?)"> *<img alt=\"Prior Strip')
    help = 'Index format: n (no padding)'


class Comet7(_BasicScraper):
    latestUrl = 'http://www.comet7.com/'
    imageUrl = 'http://www.comet7.com/archive_page.php?id=%s'
    imageSearch = compile(r'"(.*?/strips/.*?)"')
    prevSearch = compile(r'"(.*?)".*?previous_stripf')
    help = 'Index format: n (unpadded)'



class Commissioned(_BasicScraper):
    latestUrl = 'http://www.commissionedcomic.com/'
    imageUrl = 'http://www.commissionedcomic.com/index.php?strip=%s'
    imageSearch = compile(r'<img src="(http://www.commissionedcomic.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: n'



class CoolCatStudio(_BasicScraper):
    latestUrl = 'http://www.coolcatstudio.com/'
    imageUrl = 'http://www.coolcatstudio.com/index.php?p=%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r"href='(.+?)'>PREV")
    help = 'Index format: n'



class CourtingDisaster(_BasicScraper):
    latestUrl = 'http://www.courting-disaster.com/'
    imageUrl = 'http://www.courting-disaster.com/archive/%s.html'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="/images/previous.gif"[^>]+?>')
    help = 'Index format: yyyymmdd'



class CrapIDrewOnMyLunchBreak(_BasicScraper):
    latestUrl = 'http://crap.jinwicked.com/'
    imageUrl = 'http://crap.jinwicked.com/%s'
    imageSearch = compile(r'<img src="(http://crap.jinwicked.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src="http://comics.jinwicked.com/images/navigation_back.png"')
    help = 'Index format: yyyy/mm/dd/name'



class CtrlAltDel(_BasicScraper):
    latestUrl = 'http://www.cad-comic.com/cad/'
    imageSearch = compile(r'<img src="(/comics/\w+/\d{8}\..+?)"')
    prevSearch = compile(r'<a href="(/\w+/\d{8})" class="nav-back')
    help = 'Index format: yyyymmdd'

    @property
    def imageUrl(self):
        return self.latestUrl + '%s'



class CtrlAltDelSillies(CtrlAltDel):
    name = 'CtrlAltDel/Sillies'
    latestUrl = 'http://www.cad-comic.com/sillies/'

class Curvy(_BasicScraper):
    latestUrl = 'http://www.c.urvy.org/'
    imageUrl = 'http://www.c.urvy.org/?date=%s'
    imageSearch = compile(r'(/c/.+?)"')
    prevSearch = compile(r'(/\?date=.+?)">&lt;&lt; Previous page')
    help = 'Index format: yyyymmdd'


def cloneManga(name, shortName, lastStrip=None):
    baseUrl = 'http://manga.clone-army.org/%s.php' % (shortName,)
    imageUrl = baseUrl + '?page=%s'
    if lastStrip is None:
        starter = bounceStarter(baseUrl, compile(r'<a href="([^"]+)"><img src="next\.gif"'))
    else:
        starter = constStarter(imageUrl % (lastStrip,))

    def namer(self, imageUrl, pageUrl):
        return '%03d' % (int(getQueryParams(pageUrl)['page'][0]),)

    return type('CloneManga_%s' % name,
        (_BasicScraper,),
        dict(
            name='CloneManga/' + name,
            starter=starter,
            imageUrl=imageUrl,
            imageSearch=compile(r'<img src="(http://manga\.clone-army\.org/[^"]+)"'),
            prevSearch=compile(r'<a href="([^"]+)"><img src="previous\.gif"'),
            help='Index format: n',
            namer=namer)
    )


anm = cloneManga('AprilAndMay', 'anm')
kanami = cloneManga('Kanami', 'kanami')
momoka = cloneManga('MomokaCorner', 'momoka')
nana = cloneManga('NanasEverydayLife', 'nana', '78')
pxi = cloneManga('PaperEleven', 'pxi', '311')
t42r = cloneManga('Tomoyo42sRoom', 't42r')
penny = cloneManga('PennyTribute', 'penny')


class CatAndGirl(_BasicScraper):
    latestUrl = 'http://catandgirl.com/'
    imageUrl = 'http://catandgirl.com/?p=%s'
    imageSearch = compile(r'<img src="(http://catandgirl.com/archive/.+?)"')
    prevSearch = compile(r'\s+<a href="(.+?)">&#9668; Previous</a>')
    help = 'Index format: n (unpadded)'


def comicsDotCom(name, section):
    baseUrl = 'http://www.comics.com/%s/%s/archive/' % (section, name)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        htmlname = pageUrl.split('/')[-1]
        filename = htmlname.split('.')[0]
        return filename

    return type('ComicsDotCom_%s' % name,
        (_BasicScraper,),
        dict(
        name='ComicsDotCom/' + name,
        starter=indirectStarter(baseUrl, compile(r'<A HREF="(/[\w/]+?/archive/\w+?-\d{8}\.html)">(?:<IMG SRC="/[\w/]+?/images/arrow_right.gif|(?:<font[^>]*?>)?Next Day)')),
        imageUrl=baseUrl + 'name-%s.html',
        imageSearch=compile(r'SRC="(/[\w/]+?/archive/images/\w+?\d+\..+?)"'),
        prevSearch=compile(r'<A HREF="(/[\w/]+?/archive/\w+?-\d{8}\.html)">(?:<IMG SRC="/[\w/]+?/images/arrow_left.gif|(?:<font[^>]*?>)?Previous Day)'),
        help='Index format: yyyymmdd',
        namer=namer)
    )


acaseinpoint = comicsDotCom('acaseinpoint', 'comics')
agnes = comicsDotCom('agnes', 'creators')
alleyoop = comicsDotCom('alleyoop', 'comics')
andycapp = comicsDotCom('andycapp', 'creators')
arlonjanis = comicsDotCom('arlonjanis', 'comics')
ballardst = comicsDotCom('ballardst', 'creators')
barkeaterlake = comicsDotCom('barkeaterlake', 'comics')
bc = comicsDotCom('bc', 'creators')
ben = comicsDotCom('ben', 'comics')
betty = comicsDotCom('betty', 'comics')
bignate = comicsDotCom('bignate', 'comics')
bonanas = comicsDotCom('bonanas', 'wash')
bornloser = comicsDotCom('bornloser', 'comics')
buckets = comicsDotCom('buckets', 'comics')
candorville = comicsDotCom('candorville', 'wash')
cheapthrills = comicsDotCom('cheapthrills', 'wash')
chickweed = comicsDotCom('chickweed', 'comics')
committed = comicsDotCom('committed', 'comics')
dilbert = comicsDotCom('dilbert', 'comics')
drabble = comicsDotCom('drabble', 'comics')
fatcats = comicsDotCom('fatcats', 'comics')
ferdnand = comicsDotCom('ferdnand', 'comics')
flightdeck = comicsDotCom('flightdeck', 'creators')
floandfriends = comicsDotCom('floandfriends', 'creators')
franknernest = comicsDotCom('franknernest', 'comics')
frazz = comicsDotCom('frazz', 'comics')
geech = comicsDotCom('geech', 'comics')
genepool = comicsDotCom('genepool', 'wash')
getfuzzy = comicsDotCom('getfuzzy', 'comics')
gofish = comicsDotCom('gofish', 'comics')
graffiti = comicsDotCom('graffiti', 'comics')
grandave = comicsDotCom('grandave', 'comics')
grizzwells = comicsDotCom('grizzwells', 'comics')
heathcliff = comicsDotCom('heathcliff', 'creators')
hedge = comicsDotCom('hedge', 'comics')
herbnjamaal = comicsDotCom('herbnjamaal', 'creators')
herman = comicsDotCom('herman', 'comics')
humblestumble = comicsDotCom('humblestumble', 'comics')
janesworld = comicsDotCom('janesworld', 'comics')
jumpstart = comicsDotCom('jumpstart', 'comics')
kitncarlyle = comicsDotCom('kitncarlyle', 'comics')
liberty = comicsDotCom('liberty', 'creators')
lilabner = comicsDotCom('lilabner', 'comics')
luann = comicsDotCom('luann', 'comics')
marmaduke = comicsDotCom('marmaduke', 'comics')
meg = comicsDotCom('meg', 'comics')
moderatelyconfused = comicsDotCom('moderatelyconfused', 'comics')
momma = comicsDotCom('momma', 'creators')
monty = comicsDotCom('monty', 'comics')
motley = comicsDotCom('motley', 'comics')
nancy = comicsDotCom('nancy', 'comics')
naturalselection = comicsDotCom('naturalselection', 'creators')
offthemark = comicsDotCom('offthemark', 'comics')
onebighappy = comicsDotCom('onebighappy', 'creators')
othercoast = comicsDotCom('othercoast', 'creators')
pcnpixel = comicsDotCom('pcnpixel', 'wash')
peanuts = comicsDotCom('peanuts', 'comics')
pearls = comicsDotCom('pearls', 'comics')
pibgorn = comicsDotCom('pibgorn', 'comics')
pickles = comicsDotCom('pickles', 'wash')
raisingduncan = comicsDotCom('raisingduncan', 'comics')
reality = comicsDotCom('reality', 'comics')
redandrover = comicsDotCom('redandrover', 'wash')
ripleys = comicsDotCom('ripleys', 'comics')
roseisrose = comicsDotCom('roseisrose', 'comics')
rubes = comicsDotCom('rubes', 'creators')
rudypark = comicsDotCom('rudypark', 'comics')
shirleynson = comicsDotCom('shirleynson', 'comics')
soup2nutz = comicsDotCom('soup2nutz', 'comics')
speedbump = comicsDotCom('speedbump', 'creators')
spotthefrog = comicsDotCom('spotthefrog', 'comics')
strangebrew = comicsDotCom('strangebrew', 'creators')
sunshineclub = comicsDotCom('sunshineclub', 'comics')
tarzan = comicsDotCom('tarzan', 'comics')
thatslife = comicsDotCom('thatslife', 'wash')
wizardofid = comicsDotCom('wizardofid', 'creators')
workingdaze = comicsDotCom('workingdaze', 'comics')
workingitout = comicsDotCom('workingitout', 'creators')


def creators(name, shortname):
    return type('Creators_%s' % name,
        (_BasicScraper,),
        dict(
        name='Creators/' + name,
        latestUrl='http://www.creators.com/comics_show.cfm?ComicName=%s' % (shortname,),
        imageUrl=None,
        imageSearch=compile(r'<img alt="[^"]+" src="(\d{4}/.+?/.+?\..+?)">'),
        prevSearch=compile(r'<a href="(comics_show\.cfm\?next=\d+&ComicName=.+?)" Title="Previous Comic"'),
        help='Indexing unsupported')
    )


arc = creators('Archie', 'arc')
shg = creators('AskShagg', 'shg')
hev = creators('ForHeavensSake', 'hev')
rug = creators('Rugrats', 'rug')
sou = creators('StateOfTheUnion', 'sou')
din = creators('TheDinetteSet', 'din')
lil = creators('TheMeaningOfLila', 'lil')
wee = creators('WeePals', 'wee')
zhi = creators('ZackHill', 'zhi')



class CyanideAndHappiness(_BasicScraper):
    latestUrl = 'http://www.explosm.net/comics'
    imageUrl = 'http://www.explosm.net/comics/%s'
    imageSearch = compile(r'<img alt="Cyanide and Happiness, a daily webcomic" src="(http:\/\/www\.explosm\.net/db/files/Comics/\w+/\S+\.\w+)"')
    prevSearch = compile(r'<a href="(/comics/\d+/?)">< Previous</a>')
    help = 'Index format: n (unpadded)'



class CrimsonDark(_BasicScraper):
    latestUrl = 'http://www.davidcsimon.com/crimsondark/'
    imageUrl = 'http://www.davidcsimon.com/crimsondark/index.php?view=comic&strip_id=%s'
    imageSearch = compile(r'src="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href=[\'"](/crimsondark/index\.php\?view=comic&amp;strip_id=\d+)[\'"]><img src=[\'"]themes/cdtheme/images/active_prev.png[\'"]')
    help = 'Index format: n (unpadded)'



class CrimesOfCybeleCity(_BasicScraper):
    latestUrl = 'http://www.pulledpunches.com/crimes/'
    imageUrl = 'http://www.beaglespace.com/pulledpunches/crimes/?p=%s'
    imageSearch = compile(r'<img src="(http://www\.beaglespace\.com/pulledpunches/crimes/comics/[^"]+)"')
    prevSearch = compile(r'<a href="(http://www\.beaglespace\.com/pulledpunches/crimes/\?p=\d+)"><img src="back1\.gif"')
    help = 'Index format: nn'



class CatsAndCameras(_BasicScraper):
    latestUrl = 'http://catsncameras.com/cnc/'
    imageUrl = 'hhttp://catsncameras.com/cnc/?p=%s'
    imageSearch = compile(r'<img src="(http://catsncameras.com/cnc/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://catsncameras.com/cnc/.+?)">')
    help = 'Index format: nnn'



class CowboyJedi(_BasicScraper):
    latestUrl = 'http://www.cowboyjedi.com/'
    imageUrl = 'http://www.cowboyjedi.com/%s'
    imageSearch = compile(r'<img src="(http://www.cowboyjedi.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.cowboyjedi.com/.+?)" class="navi navi-prev"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class CasuallyKayla(_BasicScraper):
    latestUrl = 'http://casuallykayla.com/'
    imageUrl = 'http://casuallykayla.com/?p=%s'
    imageSearch = compile(r'<img src="(http://casuallykayla.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: nnn'



class Collar6(_BasicScraper):
    latestUrl = 'http://collar6.com/'
    imageUrl = 'http://collar6.com/%s'
    imageSearch = compile(r'src="(http://collar6.com/comics/.+?)"')
    prevSearch = compile(r' href="(http://collar6.com/\d+/\S+)">&#9668; Previous')
    help = 'Index format: yyyy/namednumber'



class Chester5000XYV(_BasicScraper):
    latestUrl = 'http://jessfink.com/Chester5000XYV/'
    imageUrl = 'http://jessfink.com/Chester5000XYV/?p=%s'
    imageSearch = compile(r'<img src="(http://jessfink.com/Chester5000XYV/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: nnn'



class CalamitiesOfNature(_BasicScraper):
    latestUrl = 'http://www.calamitiesofnature.com/'
    imageUrl = 'http://www.calamitiesofnature.com/archive/?c=%s'
    imageSearch = compile(r'<IMG SRC="(archive/\d+.+?|http://www.calamitiesofnature.com/archive/\d+.+?)"')
    prevSearch = compile(r'<a id="previous" href="(http://www.calamitiesofnature.com/archive/\?c\=\d+)">')
    help = 'Index format: nnn'



class Champ2010(_BasicScraper):
    latestUrl = 'http://www.jedcollins.com/champ2010/'
    imageUrl = 'http://jedcollins.com/champ2010/?p=%s'
    imageSearch = compile(r'<img src="(http://jedcollins.com/champ2010/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://jedcollins.com/champ2010/.+?)"')
    help = 'Index format: nnn'



class Chucklebrain(_BasicScraper):
    latestUrl = 'http://www.chucklebrain.com/main.php'
    imageUrl = 'http://www.chucklebrain.com/main.php?img=%s'
    imageSearch = compile(r'<img src="(/images/strip.+?)"')
    prevSearch = compile(r'<a href=\'(/main.php\?img\=\d+)\'><img src=\'/images/previous.jpg\'')
    help = 'Index format: nnn'



class CompanyY(_BasicScraper):
    latestUrl = 'http://company-y.com/'
    imageUrl = 'http://company-y.com/%s/'
    imageSearch = compile(r'<img src="(http://company-y.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://company-y.com/.+?)"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class CorydonCafe(_BasicScraper):
    starter = bounceStarter('http://corydoncafe.com/', compile(r' href="(\./comic-\d+.html)">Next&gt;</a>'))
    imageUrl = 'http://corydoncafe.com/comic-%s.html'
    imageSearch = compile(r'<img src=\'(\./comics/.+?)\' ')
    prevSearch = compile(r' href="(\./comic-\d+.html)">&lt;Previous</a>')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]



class CraftedFables(_BasicScraper):
    latestUrl = 'http://www.craftedfables.com/'
    imageUrl = 'http://www.caf-fiends.net/craftedfables/?p=%s'
    imageSearch = compile(r'<img src="(http://www.caf-fiends.net/craftedfables/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.caf-fiends.net/craftedfables/.+?)"><span class="prev">')
    help = 'Index format: nnn'



class Currhue(_BasicScraper):
    latestUrl = 'http://www.currhue.com/'
    imageUrl = 'http://www.currhue.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.currhue.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.currhue.com/.+?)"')
    help = 'Index format: nnn'