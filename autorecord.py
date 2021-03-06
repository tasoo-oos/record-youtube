import requests
import os
import time
import subprocess
import datetime
import pickle
import argparse


# pyinstaller --onefile autorecord.py


class TwitchRecorder:
    def __init__(self):
        # global configuration
        self.client_id = "jzkbprff40iqj646a697cyrvl0zt2m6"  # don't change this
        # get oauth token value by typing `streamlink --twitch-oauth-authenticate` in terminal
        self.refresh = 60.0
        self.recorded_path = ""

        # user configuration
        self.username = ""
        self.quality = "480p"
        self.videostatus = ""

    def run(self):
        # create directory for recordedPath and processedPath if not exist
        self.recorded_path = os.getcwd()
        if os.path.isdir(self.recorded_path) is False:
            os.makedirs(self.recorded_path)

        '''
        # make sure the interval to check user availability is not less than 15 seconds
        if self.refresh < 15:
            print("Check interval should not be lower than 15 seconds.")
            self.refresh = 15
            print("System set check interval to 15 seconds.")
        '''

        print("Checking for", self.username, "every", self.refresh, "seconds. Record with", self.quality, "quality.")
        self.loopcheck()

    def check_user(self):
        # 0: online,
        # 1: offline,
        # 2: not found,
        # 3: error
        info = None
        status = 3
        try:
            h = {"Client-ID": self.client_id, "Accept": "application/vnd.twitchtv.v5+json"}
            r = requests.get(f"https://api.twitch.tv/kraken/users?login={self.username}", headers=h)
            a = r.json()
            user_id = r.json().get("users", [{}])[0].get("_id", "")

            r = requests.get(f"https://api.twitch.tv/kraken/streams/{user_id}", headers=h, timeout=15)
            r.raise_for_status()
            info = r.json()
            if info['stream'] is None:
                status = 1
            else:
                status = 0
        except requests.exceptions.RequestException as e:
            if e.response:
                if e.response.reason == 'Not Found' or e.response.reason == 'Unprocessable Entity':
                    status = 2

        return status, info

    def loopcheck(self):
        while True:
            status, info = self.check_user()
            if status == 2:
                print("Username not found. Invalid username or typo. type again.")
                self.username = input()
            elif status == 3:
                print(datetime.datetime.now().strftime("%Hh%Mm%Ss"), " ",
                      "unexpected error. will try again in 1 minutes.")
                time.sleep(60)
            elif status == 1:
                print(self.username, "currently offline, checking again in", self.refresh, "seconds.")
                time.sleep(self.refresh)
            elif status == 0:
                print(self.username, "online. Stream recording in session.")
                filename = datetime.datetime.now().strftime("%Y%m%d") + " " \
                           + info['stream']['channel']['display_name'] + ' ' \
                           + info['stream']['channel']['status'] + ".mp4"

                recorded_filename = os.path.join(self.recorded_path, filename)

                if os.path.isfile(recorded_filename):
                    i = 1
                    original_filename = recorded_filename
                    while True:
                        i += 1
                        recorded_filename = original_filename[:-4] + str(i) + original_filename[-4:]
                        if not os.path.isfile(recorded_filename):
                            break

                # start streamlink process
                subprocess.call(
                    ["streamlink", "--twitch-disable-hosting", "--twitch-disable-ads", "twitch.tv/" + self.username,
                     self.quality, "-o", recorded_filename])

                if os.path.isfile(recorded_filename) is False:
                    subprocess.call(
                        ["streamlink", "--twitch-disable-hosting", "--twitch-disable-ads", "twitch.tv/" + self.username,
                         'best', "-o", recorded_filename])

                print("Recording stream is done.")
                arg = argparse.Namespace(auth_host_name='localhost', noauth_local_webserver=False,
                                         auth_host_port=[8080, 8090], logging_level='ERROR',
                                         file=recorded_filename, title=filename[:-4],
                                         description='', category='22',
                                         keywords='', privacyStatus=self.videostatus)
                print(arg)
                while True:
                    if not os.path.isfile(os.path.join(os.getcwd(), 'temp.pickle')):
                        with open('temp.pickle', 'wb') as f:
                            pickle.dump(arg, f)
                        break
                    time.sleep(10)
                    print("temp.pickle 파일이 삭제되기를 기다리는중....\n만약 이 메세지가 계속 뜬다면 파일을 수동으로 지우십시오")

                os.startfile(r'C:\Users\tasoo\OneDrive\Desktop\record\upload_video.exe')
                print('유투브 업로드용 프로그램 실행')
                time.sleep(self.refresh)


def main():
    try:
        twitch_recorder = TwitchRecorder()

        with open('start.pickle', 'rb') as f:
            data = pickle.load(f)
        os.remove('start.pickle')

        twitch_recorder.refresh = data[0]
        twitch_recorder.quality = data[1]
        twitch_recorder.videostatus = data[2]
        twitch_recorder.username = data[3]

        twitch_recorder.run()

    except Exception as e:
        i = 1
        while os.path.isfile(os.path.join(os.getcwd(), 'loga' + str(i) + '.txt')):
            i += 1
        with open('loga' + str(i) + '.txt', 'wt') as f:
            f.write(str(e))
        print(e)
        

if __name__ == "__main__":
    main()
