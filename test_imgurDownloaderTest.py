from imgurDownloader import mimeToExtension

def test_mimeToExtension():
    print "Testing mimeToExtension(\"image/png\")"
    assert mimeToExtension("image/png") == "png"
