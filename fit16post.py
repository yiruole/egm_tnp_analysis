import subprocess

commands = [
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 20",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 29",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 30",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 39",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 40",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 49",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 41",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 48",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 50",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 59",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 51",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 58",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 60",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 69",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 61",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 68",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 70",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 79",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 80",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 89",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 81",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 82",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 88",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 90",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 91",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 93",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 94",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 95",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 96",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 98",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --iBin 99",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 20",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 29",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 30",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 39",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 40",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 49",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 41",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 48",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 50",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 59",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 51",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 58",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 60",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 69",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 61",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 68",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 70",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 79",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 80",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 89",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 81",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 82",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 88",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 90",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 91",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 93",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 94",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 95",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 96",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 98",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --doFit --altSig --iBin 99",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post.py --flag passingTrigger --sumUp",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 64",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 71",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 72",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 74",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 75",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 76",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 77",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --iBin 79",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 64",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 71",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 72",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 74",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 75",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 76",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 77",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --doFit --altSig --iBin 79",
    "python tnpEGM_fitter.py etc/config/settings_passTrigger16post_3bins.py --flag passingTrigger --sumUp",
]

for command in commands:
    subprocess.call(command, shell=True)