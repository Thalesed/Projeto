const {app, BrowserWindow, Menu} = require('electron')
const path = require('path')

const icon = path.join(__dirname, 'img1.ico')

let win


const template = [
	{
		label: 'Teste',
		click: () => function(){
			
		}
	}
]

const createWindow = () => {
	win = new BrowserWindow({
	width: 800,
	height: 600,
	webPreferences: {
		nodeIntegration: true
	}
	})

	const menu = Menu.buildFromTemplate(template)
	win.setMenu(menu)
	win.loadFile("index.html")
}




app.whenReady().then(() => {
	//app.dock.setIcon(icon)
	createWindow()
})
