# Simple Looper malware in Go
![post](./image.png)

# Languages
- Go

#### Build command for windows:
```bash
go build -ldflags -H=windowsgui -o looper main.go
```

#### Build command for linux (cross compile):
```bash
GOOS=windows GOARCH=amd64 go build -ldflags -H=windowsgui -o looper main.go
```