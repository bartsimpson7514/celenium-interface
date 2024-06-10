/** Services */
import { useServerURL } from "@/services/config"

export const fetchHead = async () => {
	try {
		const url = new URL(`http://18.116.231.219:26657/head/`)
		const data = await $fetch(url)
		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchConstants = async () => {
	try {
		const url = new URL(`http://18.116.231.219:26657/constants/`)
		const data = await $fetch(url)
		return data
	} catch (error) {
		console.error(error)
	}
}
