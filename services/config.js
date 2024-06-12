export const Server = {
	API: {
		mainnet: "http://127.0.0.1:9876/v1",
		mocha: "http://127.0.0.1:9876/v1",
		arabica: "http://127.0.0.1:9876/v1",
		dev: "http://127.0.0.1:9876/v1",
		self: "http://127.0.0.1:9876/",
	},
	WSS: {
		mainnet: "wss://api.celenium.io/v1/ws",
		mocha: "wss://api-mocha-4.celenium.io/v1/ws",
		arabica: "wss://api-arabica-11.celenium.io/v1/ws",
		dev: "wss://api-dev.celenium.io/v1/ws",
	},
	BLOBSTREAM: {
		mainnet: "https://api-blobstream.celenium.io/v1",
		testnet: "https://api-blobstream-testnet.celenium.io/v1",
	},
}

export const useServerURL = () => {
	const requestURL = useRequestURL()

	switch (requestURL.hostname) {
		case "http://127.0.0.1:9876/":
			return Server.API.mainnet

		case "http://127.0.0.1:9876/":
			return Server.API.mocha

		case "http://127.0.0.1:9876/":
			return Server.API.mocha

		case "http://127.0.0.1:9876/":
			return Server.API.arabica

		case "http://127.0.0.1:9876/":
			return Server.API.dev

		default:
			return Server.API.arabica
	}
}

export const useSocketURL = () => {
	const requestURL = useRequestURL()

	switch (requestURL.hostname) {
		case "celenium.io":
			return Server.WSS.mainnet

		case "mocha-4.celenium.io":
			return Server.WSS.mocha

		case "mocha.celenium.io":
			return Server.WSS.mocha

		case "arabica.celenium.io":
			return Server.WSS.arabica

		case "dev.celenium.io":
			return Server.WSS.dev

		default:
			return Server.WSS.arabica
	}
}

export const useBlobstreamURL = () => {
	const requestURL = useRequestURL()

	switch (requestURL.hostname) {
		case "http://127.0.0.1:9876/":
			return Server.BLOBSTREAM.testnet

		case "http://127.0.0.1:9876/":
			return Server.BLOBSTREAM.testnet

		case "http://127.0.0.1:9876/":
			return Server.BLOBSTREAM.testnet

		default:
			return Server.BLOBSTREAM.mainnet
	}
}
