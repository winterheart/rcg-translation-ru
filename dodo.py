from io import BytesIO
from os.path import join
# import requests
# import zipfile

rcg_t = "../rcg_l10n/rcg_translate.py"

# rcg_translate_ru_version = "1.0"
# rcg_mod_version = "1.3"
# rcg_mod_url = "https://github.com/MoArtis/RCGMod/releases/download/%s/RCG-UserXpMod_STEAM_%s.zip" % (rcg_mod_version, rcg_mod_version)

SOURCE = {
    "input_json": "source/RCG_LocalizationData.json",
    "output_json": "target/RiverCityGirls_Data/StreamingAssets/LocalizationData/RCG_LocalizationData.json",
    "po_dir": "translation",
    "languages": [
        "ru",
    ],
    "po_files": [
        "Dialog_Keys.po",
        "Equip_Keys.po",
        "MetaData_Keys.po",
        "Move_Keys.po",
        "Non_Dialog_Keys.po",
        "QuestItem_Keys.po",
        "Quest_Keys.po",
        "Store_Keys.po",
        "Tutorial_Keys.po",
        "Useables_Keys.po"
    ]
}

full_po_paths = []
langs_param = ""

for lang in SOURCE["languages"]:
    langs_param += "-l %s " % lang
    for po_file in SOURCE["po_files"]:
        full_po_paths.append(join(SOURCE["po_dir"], lang, po_file))


#def task_fetch_rcg_mod():
#    """Fetch and extract RCG Mod"""
#    resp = requests.get(rcg_mod_url)
#    zip_file = zipfile.ZipFile(BytesIO(resp.content))
#    zip_file.extractall("target")


def task_make_update_po():
    """Make/Update Gettext files"""
    yield {
        "name": "make_update_po",
        "actions": ["%s extract -i %s -p %s %s" % (rcg_t, SOURCE["input_json"], SOURCE["po_dir"], langs_param)],
        "file_dep": [SOURCE["input_json"]],
        "targets": full_po_paths
    }


def task_make_json():
    """Make JSON file from PO"""
    yield {
        "name": "make_json",
        "actions":["%s pack -i %s -p %s -o %s %s" % (rcg_t, SOURCE["input_json"], SOURCE["po_dir"], SOURCE["output_json"], langs_param)],
        "file_dep": full_po_paths,
        "targets": [SOURCE["output_json"]]
    }

