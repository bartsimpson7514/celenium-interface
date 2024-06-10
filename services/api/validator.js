/** Services */
import { useServerURL } from "@/services/config"

export const fetchValidators = async ({ jailed = false, limit, offset, sort }) => {
	try {
		// const url = new URL(`${useServerURL()}/validators`)

		const url = new URL("http://18.116.231.219:26657/validators/")

		url.searchParams.append("jailed", jailed)
		if (limit) url.searchParams.append("limit", limit)
		if (offset) url.searchParams.append("offset", offset)
		if (sort) url.searchParams.append("sort", sort)

		const data = await useFetch(url.href)

		console.log("Validators data:", data)

		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorsCount = async () => {
	try {
		// const url = new URL(`${useServerURL()}/validators/count`)
		const url = new URL(`http://18.116.231.219:26657/validators/count`)

		const data = await useFetch(url.href)
		console.log("fetchValidatorsCount: ", data)
		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorByID = async (id) => {
	try {
		// const url = new URL(`${useServerURL()}/validators/${id}`)
		const url = new URL(`http://18.116.231.219:26657/validators/${id}`)

		const data = await useFetch(encodeURI(url.href))
		// console.log("fetchValidatorByID: ", data)

		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorBlocks = async ({ id, limit, offset }) => {
	try {
		const url = new URL(`${useServerURL()}/validators/${id}/blocks`)

		if (limit) url.searchParams.append("limit", limit)
		if (offset) url.searchParams.append("offset", offset)

		const data = await useFetch(encodeURI(url.href))
		console.log("/validators/${id}/blocks: ", data)
		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorDelegators = async ({ id, limit, offset }) => {
	try {
		// const url = new URL(`${useServerURL()}/validators/${id}/delegators`)
		const url = new URL(`http://18.116.231.219:26657/validators/${id}/delegators/`)

		if (limit) url.searchParams.append("limit", limit)
		if (offset) url.searchParams.append("offset", offset)

		const data = await useFetch(encodeURI(url.href))
		console.log("validators' delegators: ", data)
		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorJails = async ({ id, limit, offset }) => {
	try {
		const url = new URL(`${useServerURL()}/validators/${id}/jails`)

		if (limit) url.searchParams.append("limit", limit)
		if (offset) url.searchParams.append("offset", offset)

		const data = await useFetch(encodeURI(url.href))
		console.log("fetchValidatorJails: /validators/${id}/jails: ", data)

		return data
	} catch (error) {
		console.error(error)
	}
}

export const fetchValidatorUptime = async ({ id, limit }) => {
	try {
		const url = new URL(`${useServerURL()}/validators/${id}/uptime`)

		if (limit) url.searchParams.append("limit", limit)

		const data = await useFetch(encodeURI(url.href))
		console.log("fetchValidatorUptime ", data)

		return data
	} catch (error) {
		console.error(error)
	}
}
