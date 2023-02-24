SOURCE = 
ENTRY = ./src/Main.py
PARAMETER = $(ENTRY) -F -w $(SOURCE) --distpath $(DISTPATH) --upx-dir $(UPX)
DISTPATH = ./dist
PYINSTALLER = pyinstaller
UPX = ./tools/upx
BUILD_DIR = Main

all:rebuild

build:
	$(PYINSTALLER) $(PARAMETER)

clean:
	del /q .\\dist\\
	del /q .\\build\\
	rmdir .\\build\\$(BUILD_DIR)
	rmdir .\\build
	rmdir .\\dist

rebuild:clean build

.PHONY:clean