import time 

from valkyrie.face_detection.face_detection_demo import run as run_face_detection_demo

def run():
    start_time = time.time()
    print("-- Project Valkyrie is running! --")
    run_face_detection_demo()
    print("--- %s seconds ---" % (time.time() - start_time))
