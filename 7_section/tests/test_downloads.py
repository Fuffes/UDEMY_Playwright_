


def test_download(page):
    with page.expect_download() as download_info:
        page.get_by_text("Download file").click()
    download = download_info.value

    download.save_as("/path/to/save/at/" + download.suggested_filename)



# https://playwright.dev/python/docs/api/class-download