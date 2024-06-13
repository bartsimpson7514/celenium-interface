export const Server = {
	API: {
		mainnet: "https://api.gasguard.xyz/v1",
		mocha: "https://api.gasguard.xyz/v1",
		arabica: "https://api.gasguard.xyz/v1",
		dev: "https://api.gasguard.xyz/v1",
		self: "https://api.gasguard.xyz/",
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
		case "https://api.gasguard.xyz/":
			return Server.API.mainnet

		case "https://api.gasguard.xyz/":
			return Server.API.mocha

		case "https://api.gasguard.xyz/":
			return Server.API.mocha

		case "https://api.gasguard.xyz/":
			return Server.API.arabica

		case "https://api.gasguard.xyz/":
			return Server.API.dev

		case "selfchain.xyz":
			return Server.API.selfchain

		default:
			return Server.API.arabica
	}
}

export const useSocketURL = () => {
	const requestURL = useRequestURL()

	switch (requestURL.hostname) {
		case "celenium.io":
			return Server.WSS.mainnet

		case "mogit cha-4.celenium.io":
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
		case "https://api.gasguard.xyz/":
			return Server.BLOBSTREAM.testnet

		case "https://api.gasguard.xyz/":
			return Server.BLOBSTREAM.testnet

		case "https://api.gasguard.xyz/":
			return Server.BLOBSTREAM.testnet

		default:
			return Server.BLOBSTREAM.mainnet
	}
}
