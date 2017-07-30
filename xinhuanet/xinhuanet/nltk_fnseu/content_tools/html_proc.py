#-*- coding:utf-8-*-
import re

def removeTags(html):  # 去除标签
    reDoc = r'<!DOCTYPE.*?>'
    reComm = r'<!--.*?-->'
    reJs1 = r'<script.*?>[\s\S]*?</script>'
    reJs2 = r'<SCRIPT.*?>[\s\S]*?</SCRIPT>'
    reCss = r'<style.*?>[\s\S]*?</style>'
    reTextarea = r'<textarea.*?>[\s\S]*?</textarea>'
    reSpechar = r'&.{2,8};|&#.{2,8};'
    reNotes = r'<!--[.*]>.*?<![.*]-->'  # <!--[if !IE]>|xGv00|9900d21eb16fa4350a3001b3974a9415<![endif]-->
    reOthtag = r'<[\s\S]*?>'
    reNoImgtag = r'(<(?!(img|IMG))[\s\S]*?>)+'

    html = re.sub(reNotes, ' ', html)
    html = re.sub(reJs1, ' ', html)
    html = re.sub(reJs2, ' ', html)
    html = re.sub(reCss, ' ', html)
    html = re.sub(reTextarea, ' ', html)
    html = re.sub(reSpechar, ' ', html)
    html = re.sub(reDoc, ' ', html)
    html= re.sub(reComm, ' ', html)
    html = re.sub(reNoImgtag, ' ', html)
    html = re.sub(reOthtag, ' ', html)

    return html