import requests
import urllib.request
headers = {
        'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36",
        #'cookie':"BIDUPSID=C530A848183C273DB86011E29D4CB5AF;PSTM=1614228517; BAIDUID=C530A848183C273D4E60055638F1BF4A:FG=1; BAIDUID_BFESS=C530A848183C273D4E60055638F1BF4A:FG=1; COOKIE_SESSION=23597864_0_9_1_15_0_1_0_9_0_0_0_23597937_0_1_0_1637914518_0_1637914519%7C9%23527_3_1614246018%7C2; BD_HOME=1; BD_UPN=12314353; sugstore=0; H_PS_PSSID=34439_35104_31660_34584_34518_35234_34606_35329_35319_26350; BA_HECTOR=a4ak8l24a5058ka4o81gr2qg30q; BDUSS=2g2OVhCcVY0bHVwZDd4bHc3S1h3eW4ydDJxMjJ4SDQ5Z051TGlOeUc1VTA5OWhoSVFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADRqsWE0arFhY; BDUSS_BFESS=2g2OVhCcVY0bHVwZDd4bHc3S1h3eW4ydDJxMjJ4SDQ5Z051TGlOeUc1VTA5OWhoSVFBQUFBJCQAAAAAAAAAAAEAAADsDfNKbXp6bnFfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADRqsWE0arFhY; H_WISE_SIDS=107313_110085_127969_174441_176399_181588_182241_183035_183329_184011_184286_185240_185268_186635_186841_187282_187433_187726_187877_188331_188453_188553_189092_189712_189732_189755_190034_190473_190679_190757_190779_190796_191068_191249_191368_191418_191503_191810_192206_192237_192333_192408_192902_193040_193195_193283_193291_193348_193491_193501_193558_193758_193883_193891_194047_194085_194511_194520_194583_194603_194612_194919_194996_195047_195107_195150_195175_195189_195342_195401_195472_195478_195533_195541_195551_195591_195617_195631_195679_195764_195784_195934_196000_196037_196050_196274_196275_196382_196428_196461_196490_196754_196780; rsv_i=30a8RwOQLZL%2BJokMB6GnyY5q%2Bcw3B3RsdqFvG%2B6UIKH17RxiaCiLyrWEFusIdBFLJ3pIwOmJ2nuaTO98Vh0nzozqA8REUBM; BDSVRTM=35; plus_lsv=e9e1d7eaf5c62da9; BDORZ=AE84CDB3A529C0F8A2B9DCDD1D18B695; plus_cv=1::m:7.94e+147; Hm_lvt_12423ecbc0e2ca965d84259063d35238=1639017015; Hm_lpvt_12423ecbc0e2ca965d84259063d35238=1639017015; SE_LAUNCH=5%3A27316950_0%3A27316950"
        #'Cookie': 'SESSION=ZTNjNTIzMjYtMjBiNi00OTFmLTkxOGMtMmMxZDEyYjYwMDkx'
        'cookie': '_iuqxldmzr_=32; _ntes_nnid=faa7b386c4ef10fff9b98c77652f99c1,1617082187829; _ntes_nuid=faa7b386c4ef10fff9b98c77652f99c1; NMTID=00OVu_6UBYTUtxtcEDRugF8rk4vBO8AAAF4gZv7sw; WM_TID=zqbVAk4g%2Bq1AQFFRFAcrwZRDk7ABUV9Y; WEVNSM=1.0.0; ntes_kaola_ad=1; WNMCID=evbsxl.1623049484156.01.0; hb_MA-A756-FD6A5C629425_source=www.baidu.com; mp_MA-A756-FD6A5C629425_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fyunxin.163.com%2Factivity%2Fim%3Ffrom%3Dbd2jjff14499%22%2C%22updatedTime%22%3A%201638085845638%2C%22sessionStartTime%22%3A%201638085845635%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%202%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22c79c602f-63d8-4b73-9400-fc5951aaa869%22%2C%22persistedTime%22%3A%201638085845631%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201638085845638%7D%2C%22sessionUuid%22%3A%20%22b6b40446-c311-4d9a-93a8-1a4982c48603%22%7D; JSESSIONID-WYYY=28so0TqHIKDUMs6Ug1CSMz8c%2BKVcFyX8ki%5CgF2W%5C%5CN8%5CdsC0nS103PG6aNzgjzwayloHeexH8MX%2Fjh9rPR0ioA%2BQF%2F9%2Bai4x4g5i79ql3084OucSNUex%2FRcg9WQQxsU270SXhZwg4RsaZNkStiRVGAUA%5Cy%2Fr%5C0%2B7Kne%2Bj6JJJl8aWNf1%3A1639142326123; WM_NI=TIh8PERT6zzlvvRwJzQaBwfHL%2Fqumhl9ryaC1wkyo7Sim6dWBBcmtdnpjv%2Fw277r6l25isk6q0IERFRa7pOdihPilzmFpd81RbIV78yXHjC888hc6VcMpiXBNRHDl5IVWVA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eebbf17090bbacaef369acb48bb6d45b878e8a85f87cfca8a9b0c57b93b2a583e92af0fea7c3b92a9897a8d9d34f928cfa9bf968b6aa9e98c97293bf8e98e54490f1bf96f064b0e7be9ae449f3a9a59aee3d91b7a3d7e75d829ead8ef770aeb0a697ae7df2e9f993b568f2eba794ea3eb3f087a6d14e92bff991ce70abb8a08aef72af9ac085bb3b92be87b7b634bb88888bc234fce8a884b55ea193c08adb4a8e8e88a5ef3f8b8a99b7c437e2a3'
    }
#url = "https://v.qq.com/"
url = "https://music.163.com/"
responst = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(responst)
urllib.request.urlretrieve(url,'music.html')
print(response.read().decode('utf-8'))