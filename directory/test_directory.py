import local_directory

TEST_DIRECTORY_DATA = """{
    "type": "directory.Directory", 
    "people": [
        {
            "type": "directory.Person", 
            "user_id": "cybersabrina",
            "name": "Sabrina Williams",
            "bio": "awesome",
            "image_url": "http://foo"
        }, 
        {
            "type": "directory.Person", 
            "user_id": "raph44",
            "name": "Raphael Majma",
            "bio": "ninja turtle",
            "image_url": "http://bar"
        }
    ]
}
"""

def TestDirectory():
    return local_directory.LocalDirectory.from_json(TEST_DIRECTORY_DATA)