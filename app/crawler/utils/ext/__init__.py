from app.ext.utils.Performance import Performance
from app.crawler.utils.kr.kcdcAPI import kcdcAPI
import re


KcdcApi = kcdcAPI


async def cleanText(text):
    loop = Performance()
    # cleanT = await loop.run_in_executor(None, re.sub, "<.+?>", "", str(text), 0, re.I|re.S)
    cleanT = await loop.run_in_threadpool(lambda: re.sub("<.+?>", "", str(text), 0, re.I|re.S))
    return cleanT

def chunker(seq, size=3):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

async def StringToInteger(string):
    """StringToInteger는 float Type은 처리 할 수 없습니다.\n
    Only String To Integer
    """
    loop = Performance()
    __Integer = await loop.run_in_threadpool(lambda: string.replace(",", '').replace("(", '').replace(")", '').replace(",", '').replace(" ", '').replace("전일대비", '').strip())
    converted = int(__Integer)
    return converted


async def JsonData(listdata):
    jsondata = [
        {"SEOUL":{"increase": float(listdata[5]),"cases": float(listdata[6]),"deaths": float(listdata[7]),"ratio": float(listdata[8]),"inspection": float(listdata[9])}},
        {"BUSAN":{"increase": float(listdata[10]),"cases": float(listdata[11]),"deaths": float(listdata[12]),"ratio": float(listdata[13]),"inspection": float(listdata[14])}},
        {"DAEGU":{"increase": float(listdata[15]),"cases": float(listdata[16]),"deaths": float(listdata[17]),"ratio": float(listdata[18]),"inspection": float(listdata[19])}},
        {"INCHEON":{"increase": float(listdata[20]),"cases": float(listdata[21]),"deaths": float(listdata[22]),"ratio": float(listdata[23]),"inspection": float(listdata[24])}},
        {"GWANGJU":{"increase": float(listdata[25]),"cases": float(listdata[26]),"deaths": float(listdata[27]),"ratio": float(listdata[28]),"inspection": float(listdata[29])}},
        {"DAEJEON":{"increase": float(listdata[30]),"cases": float(listdata[31]),"deaths": float(listdata[32]),"ratio": float(listdata[33]),"inspection": float(listdata[34])}},
        {"ULSAN":{"increase": float(listdata[35]),"cases": float(listdata[36]),"deaths": float(listdata[37]),"ratio": float(listdata[38]),"inspection": float(listdata[39])}},
        {"SEJONG":{"increase": float(listdata[40]),"cases": float(listdata[41]),"deaths": float(listdata[42]),"ratio": float(listdata[43]),"inspection": float(listdata[44])}},
        {"GYEONGGI":{"increase": float(listdata[45]),"cases": float(listdata[46]),"deaths": float(listdata[47]),"ratio": float(listdata[48]),"inspection": float(listdata[49])}},
        {"GANGWON":{"increase": float(listdata[50]),"cases": float(listdata[51]),"deaths": float(listdata[52]),"ratio": float(listdata[53]),"inspection": float(listdata[54])}},
        {"CHUNGBUK":{"increase": float(listdata[55]),"cases": float(listdata[56]),"deaths": float(listdata[57]),"ratio": float(listdata[58]),"inspection": float(listdata[59])}},
        {"CHUNGNAM":{"increase": float(listdata[60]),"cases": float(listdata[61]),"deaths": float(listdata[62]),"ratio": float(listdata[63]),"inspection": float(listdata[64])}},
        {"JEONBUK":{"increase": float(listdata[65]),"cases": float(listdata[66]),"deaths": float(listdata[67]),"ratio": float(listdata[68]),"inspection": float(listdata[69])}},
        {"JEONNAM":{"increase": float(listdata[70]),"cases": float(listdata[71]),"deaths": float(listdata[72]),"ratio": float(listdata[73]),"inspection": float(listdata[74])}},
        {"GYEONGBUK":{"increase": float(listdata[75]),"cases": float(listdata[76]),"deaths": float(listdata[77]),"ratio": float(listdata[78]),"inspection": float(listdata[79])}},
        {"GYEONGNAM":{"increase": float(listdata[80]),"cases": float(listdata[81]),"deaths": float(listdata[82]),"ratio": float(listdata[83]),"inspection": float(listdata[84])}},
        {"JEJU":{"increase": float(listdata[85]),"cases": float(listdata[86]),"deaths": float(listdata[87]),"ratio": float(listdata[88]),"inspection": float(listdata[89])}}
    ]
    return jsondata


async def EuroJsonData(listdata):
    euroJsonData = {"result": [
        {"country": "it", "cases": int(listdata[1]), "deaths": int(listdata[2])},
        {"country": "es", "cases": int(listdata[4]), "deaths": int(listdata[5])},
        {"country": "fr", "cases": int(listdata[7]), "deaths": int(listdata[8])},
        {"country": "de", "cases": int(listdata[10]), "deaths": int(listdata[11])},
        {"country": "gb", "cases": int(listdata[13]), "deaths": int(listdata[14])},
        {"country": "nl", "cases": int(listdata[16]), "deaths": int(listdata[17])},
        {"country": "at", "cases": int(listdata[19]), "deaths": int(listdata[20])},
        {"country": "no", "cases": int(listdata[22]), "deaths": int(listdata[23])},
        {"country": "be", "cases": int(listdata[25]), "deaths": int(listdata[26])},
        {"country": "se", "cases": int(listdata[28]), "deaths": int(listdata[29])},
        {"country": "dk", "cases": int(listdata[31]), "deaths": int(listdata[32])},
        {"country": "pt", "cases": int(listdata[34]), "deaths": int(listdata[35])},
        {"country": "cz", "cases": int(listdata[37]), "deaths": int(listdata[38])},
        {"country": "gr", "cases": int(listdata[40]), "deaths": int(listdata[41])},
        {"country": "fi", "cases": int(listdata[43]), "deaths": int(listdata[44])},
        {"country": "ie", "cases": int(listdata[46]), "deaths": int(listdata[47])},
        {"country": "si", "cases": int(listdata[49]), "deaths": int(listdata[50])},
        {"country": "is", "cases": int(listdata[52]), "deaths": int(listdata[53])},
        {"country": "pl", "cases": int(listdata[55]), "deaths": int(listdata[56])},
        {"country": "ee", "cases": int(listdata[58]), "deaths": int(listdata[59])},
        {"country": "ro", "cases": int(listdata[61]), "deaths": int(listdata[62])},
        {"country": "lu", "cases": int(listdata[64]), "deaths": int(listdata[65])},
        {"country": "sk", "cases": int(listdata[67]), "deaths": int(listdata[68])},
        {"country": "bg", "cases": int(listdata[70]), "deaths": int(listdata[71])},
        {"country": "hr", "cases": int(listdata[73]), "deaths": int(listdata[74])},
        {"country": "lv", "cases": int(listdata[76]), "deaths": int(listdata[77])},
        {"country": "hu", "cases": int(listdata[79]), "deaths": int(listdata[80])},
        {"country": "cy", "cases": int(listdata[82]), "deaths": int(listdata[83])},
        {"country": "mt", "cases": int(listdata[85]), "deaths": int(listdata[86])},
        {"country": "lt", "cases": int(listdata[88]), "deaths": int(listdata[89])},
        {"country": "li", "cases": int(listdata[91]), "deaths": int(listdata[92])}
    ], "total": {"cases": int(listdata[94]), "deaths": int(listdata[95])}
    }
    return euroJsonData


async def NewsNogadaJsonData(a, b, c, d):
    """노가다"""
    #TODO: 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다 노가다
    jsondata =[
        {
            "press": a[0],
            "title": b[0],
            "summary": c[0],
            "link": d[0]
        },
        {
            "press": a[1],
            "title": b[1],
            "summary": c[1],
            "link": d[1]
        },
        {
            "press": a[2],
            "title": b[2],
            "summary": c[2],
            "link": d[2]
        },
        {
            "press": a[3],
            "title": b[3],
            "summary": c[3],
            "link": d[3]
        },
        {
            "press": a[4],
            "title": b[4],
            "summary": c[4],
            "link": d[4]
        },
        {
            "press": a[5],
            "title": b[5],
            "summary": c[5],
            "link": d[5]
        },
        {
            "press": a[6],
            "title": b[6],
            "summary": c[6],
            "link": d[6]
        },
        {
            "press": a[7],
            "title": b[7],
            "summary": c[7],
            "link": d[7]
        },
        {
            "press": a[8],
            "title": b[8],
            "summary": c[8],
            "link": d[8]
        },
        {
            "press": a[9],
            "title": b[9],
            "summary": c[9],
            "link": d[9]
        }
    ]
    return jsondata