from file_system_composite import File, Folder


def test_file_show(capsys):
    file = File("report.txt")

    file.show()

    captured = capsys.readouterr()
    assert captured.out.strip() == "report.txt"


def test_folder_show(capsys):
    folder = Folder("Documents")
    folder.add(File("report.txt"))

    folder.show()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "Documents",
        "report.txt"
    ]
