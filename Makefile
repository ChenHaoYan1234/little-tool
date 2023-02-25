SOURCE = -p ./src/defines.py -p ./src/ui/MainWindow.py -p ./src/ui/SpyderDialog.py -p ./src/ui/VideoDialog.py -p ./src/ui/__init__.py -p ./src/util/spyder.py -p ./src/util/tools.py -p ./src/util/video.py -p ./src/util/__init__.py 
ENTRY = ./src/Main.py
PARAMETER = $(ENTRY) -F -w $(SOURCE) --distpath $(DISTPATH) --upx-dir $(UPX)
DISTPATH = ./dist
PYINSTALLER = pyinstaller
UPX = ./tools/upx
BUILD_NAME = Main

all:build

build:
	$(PYINSTALLER) $(PARAMETER)

clean:
	del /F /S .\\dist\\
	del /F /S .\\build\\
	del /F .\\$(BUILD_NAME).spec
	rmdir .\\build\\$(BUILD_NAME)\\localpycs
	rmdir .\\build\\$(BUILD_NAME)
	rmdir .\\build
	rmdir .\\dist

rebuild:
	make -r clean
	make -r build

.PHONY:clean