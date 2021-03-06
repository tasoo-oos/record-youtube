# record-youtube
자동 트위치 방송 녹화 및 자동업로드

automatically record twitch streams and upload it on youtube

제가 바빠서 업뎃은 많지 않을겁니다

I am busy so don`t expect updates or bugfixes so much plz.

## requirements

이 프로그램을 쓰려면 세개의 exe파일을 한 폴더에 넣고 거기에 settings.txt 를 만들어야 합니다

you need to put three .exe`s in one folder and make settings.txt in it.

첫번째 줄엔 몇 초에 한번 방송이 켜져있나 탐색할지를, 
두번째 줄엔 녹화하고 싶은 화질을, 
세번째 줄엔 유투브에 어떤 상태로 영상을 올릴지(공개 -> public, 비공개 -> private, 일부공개 -> unlisted),
네번째 줄부턴 녹화하고싶은 스트리머 id 를 쓰면 됩니다.

중간에 빈 줄이 있어도 괜찮습니다.

In the first line, type number how freaquently check if the broadcast is on in seconds.
In the second line, type the quality you want to record(480p, 1080p60, best, worst, etc).
In the third line, type how the video will be uploaded on YouTube (public -> public, private -> private, watch videos via link -> unlisted)
From the fourth line, type channel id you want to record.

It is okay to have empty lines in middle.

또한 이 프로그램을 쓰려면 client_secrets.json 파일이 필요하고, 몇가지 인증이 필요합니다

you also need to make client_secrets.json file and a few certification

이를 위해 아래 사이트를 확인해주세요.

please check link below to do that.

https://kminito.tistory.com/5

이 모든 것이 끝났다면 master.exe 를 실행하시면 됩니다

and lastly, execute master.exe


## reference

https://kminito.tistory.com/5

https://github.com/googleapis/google-api-python-client
