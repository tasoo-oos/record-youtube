# record-youtube
자동 트위치 방송 녹화 및 자동업로드

automatically record twitch streams and upload it on youtube

제가 바빠서 업뎃은 없을겁니다

I am busy so updates or bugfixes are unavaluable.

## requirements
만약 아직 스트림링크가 없다면 https://streamlink.github.io/ 에서 다운받으십시오. 환경변수에 프로그램이 추가되어야 합니다.

if you don't have streamlink, download it in https://streamlink.github.io/. The program must be added to the environment variable.


이 프로그램을 쓰려면 세개의 exe파일을 한 폴더에 넣고 거기에 settings.txt 를 만들어야 합니다

you need to put three .exe files in one folder and make settings.txt in it.

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

녹화가 끝나고 영상을 유투브에 업로드할 때 프로그램이 몇몇 인증을 요구할겁니다

after program finishes recording and uploading video to youtube, program is going to demand a few certification.

client_secrets.json 파일을 만들거나 인증에 대해 더 자세한 정보를 확인하고 싶으시다면 아래 사이트를 확인해주세요.

please check link below to make client_secrets.json or ger more specific information about certification..

https://kminito.tistory.com/5

이 모든 것이 끝났다면 master.exe 를 실행하시면 됩니다

and lastly, execute master.exe

다른 어떤 프로그램도 실행하지 않으셔도 됩니다

you don't need to execute any other program


## reference

https://kminito.tistory.com/5

https://www.godo.dev/tutorials/python-record-twitch/

https://github.com/googleapis/google-api-python-client
