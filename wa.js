const { default: makeWASocket, useMultiFileAuthState } = require('@whiskeysockets/baileys')
const qrcode = require('qrcode-terminal')

async function start() {
    const { state, saveCreds } = await useMultiFileAuthState('auth_info')

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: true
    })

    sock.ev.on('creds.update', saveCreds)

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect, qr } = update
        if (qr) {
            qrcode.generate(qr, { small: true })
        }
        if (connection === 'open') {
            console.log('✅ WhatsApp Connected!')
        }
    })

    // Contoh kirim pesan otomatis
    sock.ev.on('messages.upsert', async (m) => {
        console.log('Pesan masuk:', m)
    })

    // Fungsi kirim pesan
    global.sendWa = async (nomor, pesan) => {
        await sock.sendMessage(nomor + '@s.whatsapp.net', { text: pesan })
        console.log('📩 Pesan terkirim ke:', nomor)
    }
}

start()
