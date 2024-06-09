<script setup>
/**
 * Composable
 */
import { useOutside } from "@/composables/outside"

/** Services */
import { isMac, getNetworkName } from "@/services/utils/general"

/** UI */
import { Dropdown, DropdownItem, DropdownTitle } from "@/components/ui/Dropdown"
import Tooltip from "@/components/ui/Tooltip.vue"
import Button from "@/components/ui/Button.vue"
import Kbd from "@/components/ui/Kbd.vue"

/** Store */
import { useAppStore } from "@/store/app"
const appStore = useAppStore()

const route = useRoute()

let removeOutside = null
const headerEl = ref(null)
const showPopup = ref(false)

const head = computed(() => appStore.lastHead)

watch(
	() => showPopup.value,
	() => {
		if (showPopup.value === true) {
			nextTick(() => {
				removeOutside = useOutside(headerEl.value.wrapper, () => {
					showPopup.value = false
				})
			})
		} else {
			removeOutside()
		}
	},
)

const isActive = (link) => {
	const splittedPath = route.path.split("/").filter(Boolean)

	switch (link) {
		case "index":
			return route.path === "/"

		case "txs":
			return splittedPath.includes("tx") || splittedPath.includes("txs")

		case "blocks":
			return splittedPath.includes("block") || splittedPath.includes("blocks")

		case "namespaces":
			return splittedPath.includes("namespace") || splittedPath.includes("namespaces")

		case "rollups":
			return splittedPath.includes("rollup") || splittedPath.includes("rollups")

		case "validators":
			return splittedPath.includes("validator") || splittedPath.includes("validators")

		default:
			break
	}
}

const handleNavigate = (url) => {
	window.location.replace(url)
}
</script>

<template>
	<Flex tag="header" ref="headerEl" justify="center" wide :class="$style.wrapper">
		<Flex align="center" justify="between" wide :class="$style.container">
			<Flex align="center" gap="8">
				<Flex @click="showPopup = !showPopup" align="center" gap="8" :class="[$style.button, $style.menu]">
					<Icon :name="!showPopup ? 'menu' : 'close'" size="16" color="secondary" />
				</Flex>

				<NuxtLink to="/">
					<Flex align="center" gap="12">
						<!-- <Icon name="logo" size="18" color="white" :class="$style.logo" /> -->

						<!-- <svg width="96" height="16" viewBox="0 0 96 16" xmlns="http://www.w3.org/2000/svg" :class="$style.logo_name">
							<path
								d="M14.22 10.46C14.0867 11.46 13.7333 12.32 13.16 13.04C12.5867 13.7467 11.82 14.2933 10.86 14.68C9.91333 15.0533 8.80667 15.24 7.54 15.24C6.44667 15.24 5.44 15.0933 4.52 14.8C3.61333 14.5067 2.82 14.08 2.14 13.52C1.47333 12.9467 0.953333 12.2467 0.58 11.42C0.22 10.58 0.04 9.62 0.04 8.54C0.04 7.44667 0.22 6.48667 0.58 5.66C0.953333 4.83333 1.47333 4.13333 2.14 3.56C2.82 2.97333 3.61333 2.53333 4.52 2.24C5.44 1.94667 6.44667 1.8 7.54 1.8C8.82 1.8 9.93333 1.99333 10.88 2.38C11.84 2.76667 12.6067 3.32 13.18 4.04C13.7533 4.76 14.1 5.62667 14.22 6.64H12.02C11.8333 6.04 11.54 5.53333 11.14 5.12C10.74 4.69333 10.2333 4.36667 9.62 4.14C9.02 3.91333 8.32667 3.8 7.54 3.8C6.55333 3.8 5.66667 3.98667 4.88 4.36C4.09333 4.72 3.47333 5.25333 3.02 5.96C2.58 6.65333 2.36 7.51333 2.36 8.54C2.36 9.55333 2.58 10.4133 3.02 11.12C3.47333 11.8133 4.09333 12.34 4.88 12.7C5.66667 13.06 6.55333 13.24 7.54 13.24C8.32667 13.24 9.02 13.1333 9.62 12.92C10.22 12.6933 10.72 12.3733 11.12 11.96C11.52 11.5333 11.8133 11.0333 12 10.46H14.22ZM24.8295 11.72H26.9695C26.8629 12.4 26.5962 13.0067 26.1695 13.54C25.7562 14.06 25.1895 14.4733 24.4695 14.78C23.7495 15.0733 22.8895 15.22 21.8895 15.22C20.7562 15.22 19.7429 15.0133 18.8495 14.6C17.9562 14.1733 17.2562 13.5733 16.7495 12.8C16.2429 12.0267 15.9895 11.1067 15.9895 10.04C15.9895 8.98667 16.2362 8.06667 16.7295 7.28C17.2229 6.49333 17.9029 5.88667 18.7695 5.46C19.6495 5.03333 20.6629 4.82 21.8095 4.82C22.9962 4.82 23.9829 5.03333 24.7695 5.46C25.5695 5.87333 26.1629 6.5 26.5495 7.34C26.9362 8.16667 27.0962 9.21333 27.0295 10.48H18.2495C18.3162 11.04 18.4962 11.5467 18.7895 12C19.0962 12.44 19.5095 12.7867 20.0295 13.04C20.5495 13.28 21.1562 13.4 21.8495 13.4C22.6229 13.4 23.2695 13.2467 23.7895 12.94C24.3229 12.6333 24.6695 12.2267 24.8295 11.72ZM21.7495 6.62C20.8429 6.62 20.0962 6.84667 19.5095 7.3C18.9229 7.74 18.5429 8.30667 18.3695 9H24.7895C24.7362 8.25333 24.4362 7.67333 23.8895 7.26C23.3429 6.83333 22.6295 6.62 21.7495 6.62ZM29.2095 1.04H31.4295V15H29.2095V1.04ZM42.4467 11.72H44.5867C44.4801 12.4 44.2134 13.0067 43.7867 13.54C43.3734 14.06 42.8067 14.4733 42.0867 14.78C41.3667 15.0733 40.5067 15.22 39.5067 15.22C38.3734 15.22 37.3601 15.0133 36.4667 14.6C35.5734 14.1733 34.8734 13.5733 34.3667 12.8C33.8601 12.0267 33.6067 11.1067 33.6067 10.04C33.6067 8.98667 33.8534 8.06667 34.3467 7.28C34.8401 6.49333 35.5201 5.88667 36.3867 5.46C37.2667 5.03333 38.2801 4.82 39.4267 4.82C40.6134 4.82 41.6001 5.03333 42.3867 5.46C43.1867 5.87333 43.7801 6.5 44.1667 7.34C44.5534 8.16667 44.7134 9.21333 44.6467 10.48H35.8667C35.9334 11.04 36.1134 11.5467 36.4067 12C36.7134 12.44 37.1267 12.7867 37.6467 13.04C38.1667 13.28 38.7734 13.4 39.4667 13.4C40.2401 13.4 40.8867 13.2467 41.4067 12.94C41.9401 12.6333 42.2867 12.2267 42.4467 11.72ZM39.3667 6.62C38.4601 6.62 37.7134 6.84667 37.1267 7.3C36.5401 7.74 36.1601 8.30667 35.9867 9H42.4067C42.3534 8.25333 42.0534 7.67333 41.5067 7.26C40.9601 6.83333 40.2467 6.62 39.3667 6.62ZM46.6267 5.04H48.8467V15H46.6267V5.04ZM53.0467 4.82C53.6201 4.82 54.1467 4.9 54.6267 5.06C55.1201 5.22 55.5401 5.46667 55.8867 5.8C56.2467 6.12 56.5201 6.52 56.7067 7C56.9067 7.48 57.0067 8.04667 57.0067 8.7V15H54.7867V9.14C54.7867 8.32667 54.5867 7.72667 54.1867 7.34C53.8001 6.94 53.1867 6.74 52.3467 6.74C51.7067 6.74 51.1201 6.88 50.5867 7.16C50.0667 7.42667 49.6401 7.78 49.3067 8.22C48.9734 8.64667 48.7801 9.12 48.7267 9.64L48.7067 8.56C48.7734 8.06667 48.9201 7.6 49.1467 7.16C49.3734 6.70667 49.6734 6.30667 50.0467 5.96C50.4201 5.6 50.8601 5.32 51.3667 5.12C51.8734 4.92 52.4334 4.82 53.0467 4.82ZM62.0588 0.819999V2.96H59.3988V0.819999H62.0588ZM59.5988 5.04H61.8388V15H59.5988V5.04ZM74.8778 15H72.6578V5.04H74.8778V15ZM72.7778 10.26L72.7978 10.9C72.7711 11.0733 72.7111 11.3333 72.6178 11.68C72.5378 12.0267 72.3978 12.4067 72.1978 12.82C72.0111 13.22 71.7578 13.6067 71.4378 13.98C71.1311 14.34 70.7445 14.64 70.2778 14.88C69.8111 15.1067 69.2445 15.22 68.5778 15.22C68.0978 15.22 67.6111 15.1533 67.1178 15.02C66.6378 14.9 66.1978 14.6933 65.7978 14.4C65.4111 14.1067 65.0978 13.7067 64.8578 13.2C64.6178 12.6933 64.4978 12.0533 64.4978 11.28V5.04H66.7178V10.86C66.7178 11.4867 66.8178 11.98 67.0178 12.34C67.2311 12.6867 67.5245 12.9333 67.8978 13.08C68.2711 13.2267 68.7045 13.3 69.1978 13.3C69.9045 13.3 70.5045 13.14 70.9978 12.82C71.4911 12.5 71.8845 12.1067 72.1778 11.64C72.4845 11.16 72.6845 10.7 72.7778 10.26ZM77.3298 5.04H79.5498V15H77.3298V5.04ZM83.7498 4.82C84.3232 4.82 84.8498 4.9 85.3298 5.06C85.8232 5.22 86.2432 5.46667 86.5898 5.8C86.9498 6.12 87.2232 6.52 87.4098 7C87.6098 7.48 87.7098 8.04667 87.7098 8.7V15H85.4898V9.14C85.4898 8.32667 85.2898 7.72667 84.8898 7.34C84.5032 6.94 83.8898 6.74 83.0498 6.74C82.4098 6.74 81.8232 6.88 81.2898 7.16C80.7698 7.42667 80.3432 7.78 80.0098 8.22C79.6765 8.64667 79.4832 9.12 79.4298 9.64L79.4098 8.56C79.4765 8.06667 79.6232 7.6 79.8498 7.16C80.0765 6.70667 80.3765 6.30667 80.7498 5.96C81.1232 5.6 81.5632 5.32 82.0698 5.12C82.5765 4.92 83.1365 4.82 83.7498 4.82ZM91.6898 4.82C92.2765 4.82 92.8098 4.9 93.2898 5.06C93.7698 5.22 94.1832 5.46667 94.5298 5.8C94.8898 6.12 95.1698 6.52 95.3698 7C95.5698 7.48 95.6698 8.04667 95.6698 8.7V15H93.4298V9.14C93.4298 8.32667 93.2298 7.72667 92.8298 7.34C92.4432 6.94 91.8298 6.74 90.9898 6.74C90.3498 6.74 89.7632 6.88 89.2298 7.16C88.7098 7.42667 88.2832 7.78 87.9498 8.22C87.6298 8.64667 87.4432 9.12 87.3898 9.64L87.3498 8.52C87.4165 8.04 87.5698 7.58 87.8098 7.14C88.0498 6.68667 88.3565 6.28667 88.7298 5.94C89.1032 5.59333 89.5365 5.32 90.0298 5.12C90.5365 4.92 91.0898 4.82 91.6898 4.82Z"
							/>
						</svg> -->

						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 359.92 76.52" :class="$style.logo_name" style="height: 25px">
							<defs>
								<component :is="'style'">.cls-1 { fill: #252641; } .cls-2 { fill: #6c11ff; }</component>
							</defs>
							<g id="Layer_2" data-name="Layer 2">
								<g id="Layer_1-2" data-name="Layer 1">
									<path
										d="M116.21,57.41a24,24,0,0,1-8.9-1.47,11.66,11.66,0,0,1-5.59-4.39,12.89,12.89,0,0,1-1.91-7.24V44h7.76v1a4.92,4.92,0,0,0,.7,2.78,4.22,4.22,0,0,0,2.56,1.55,21.65,21.65,0,0,0,5.38.5,23.83,23.83,0,0,0,4.76-.36,3.87,3.87,0,0,0,2.28-1.14,3.09,3.09,0,0,0,.62-2,2.88,2.88,0,0,0-1.06-2.5,9.57,9.57,0,0,0-3.7-1.28L109.38,41a16.13,16.13,0,0,1-5.3-1.83,9,9,0,0,1-3.4-3.41,10.59,10.59,0,0,1-1.19-5.19,10.73,10.73,0,0,1,.86-4.16,10.06,10.06,0,0,1,2.72-3.7A13.82,13.82,0,0,1,108,20.11a23.78,23.78,0,0,1,7.42-1,20.5,20.5,0,0,1,8.78,1.64,11.3,11.3,0,0,1,5.14,4.6A13.51,13.51,0,0,1,131,32.21v.33H123.2v-.78a5.39,5.39,0,0,0-.7-2.88,4.24,4.24,0,0,0-2.56-1.64,20.76,20.76,0,0,0-5.33-.53,19.2,19.2,0,0,0-4.38.39A4.26,4.26,0,0,0,108,28.27a2.93,2.93,0,0,0-.67,2,3.39,3.39,0,0,0,.41,1.74A2.73,2.73,0,0,0,109,33.1a10.57,10.57,0,0,0,2.33.66l9.73,1.67a16.42,16.42,0,0,1,6.18,2.16,9.1,9.1,0,0,1,3.34,3.64,10.6,10.6,0,0,1,1,4.69,10.56,10.56,0,0,1-6.52,9.88A21,21,0,0,1,116.21,57.41Z"
									/>
									<path
										d="M150.08,57.41a17.63,17.63,0,0,1-7.61-1.56,11.18,11.18,0,0,1-5.13-4.77,16.45,16.45,0,0,1-1.81-8.1,15.61,15.61,0,0,1,1.81-7.69,12.58,12.58,0,0,1,5-5,15.35,15.35,0,0,1,7.53-1.78A16.86,16.86,0,0,1,157.35,30a11.4,11.4,0,0,1,4.94,4.58A14.45,14.45,0,0,1,164.05,42c0,.48,0,.92-.05,1.33s-.09.85-.16,1.33H140.55V40.26h17.81L156.6,43V40.92c0-2.11-.54-3.62-1.61-4.55S152.18,35,149.76,35q-3.93,0-5.48,1.64c-1,1.09-1.55,2.82-1.55,5.19v2.11c0,2.37.51,4.1,1.55,5.19s2.88,1.64,5.54,1.64c2.27,0,3.88-.32,4.81-1a3.08,3.08,0,0,0,1.4-2.72v-.55h7.76v.61a8.79,8.79,0,0,1-1.71,5.33,11.16,11.16,0,0,1-4.79,3.63A18.38,18.38,0,0,1,150.08,57.41Z"
									/>
									<path d="M176.19,56.85h-7.76V19.66h7.76Z" />
									<path
										d="M199.07,35.93H179.61V29h19.46Zm-8,20.92h-7.76V30.93a11,11,0,0,1,1.52-5.85,10.31,10.31,0,0,1,4.56-4,17.16,17.16,0,0,1,7.42-1.45h2.28v6.05h-3.52c-2,0-3.38.33-4.14,1s-.88,2-.36,4.08V56.85Z"
									/>
									<path
										d="M232.92,57.41a19.68,19.68,0,0,1-9.86-2.36,16,16,0,0,1-6.42-6.66,21.59,21.59,0,0,1-2.25-10.13,21.56,21.56,0,0,1,2.25-10.13,16,16,0,0,1,6.42-6.66,19.68,19.68,0,0,1,9.86-2.36,22.22,22.22,0,0,1,9.39,1.83,14.11,14.11,0,0,1,6.13,5.22,14.79,14.79,0,0,1,2.17,8.16v.83H242v-.83c0-2.44-.7-4.26-2.09-5.44s-3.67-1.78-6.81-1.78A14.43,14.43,0,0,0,227,28.18a6.61,6.61,0,0,0-3.34,3.5,17.07,17.07,0,0,0-1,6.58,17.11,17.11,0,0,0,1,6.55A6.55,6.55,0,0,0,227,48.33a14.43,14.43,0,0,0,6.08,1.08q4.71,0,6.81-1.77A6.77,6.77,0,0,0,242,42.2v-.83h8.64v.83a14.83,14.83,0,0,1-2.17,8.13,14.11,14.11,0,0,1-6.13,5.25A22.22,22.22,0,0,1,232.92,57.41Z"
									/>
									<path
										d="M262.53,56.85h-7.76V19.66h7.76Zm21.32,0h-7.76V42.31q0-3.5-1.53-4.91c-1-.95-2.75-1.42-5.2-1.42a9,9,0,0,0-4.09.78,4.44,4.44,0,0,0-2.12,2.3,10.43,10.43,0,0,0-.62,3.86h-1.14l.11-5.38H263a13.27,13.27,0,0,1,1.6-4.44,9,9,0,0,1,3.39-3.33,10.85,10.85,0,0,1,5.51-1.28,10.51,10.51,0,0,1,5.8,1.5A9.18,9.18,0,0,1,282.72,34a14.18,14.18,0,0,1,1.13,5.77Z"
									/>
									<path
										d="M297,57.41a9.94,9.94,0,0,1-6.57-2,7.43,7.43,0,0,1-1.45-9A6.59,6.59,0,0,1,291.73,44a14.53,14.53,0,0,1,4.66-1.25L308,41.42v4.77l-9.53,1.17a4.17,4.17,0,0,0-2,.58,1.72,1.72,0,0,0-.65,1.47,1.74,1.74,0,0,0,.83,1.61,5,5,0,0,0,2.54.5,16,16,0,0,0,4.6-.55,5.3,5.3,0,0,0,2.77-1.81,5.35,5.35,0,0,0,1-3.35l.72-.06v4.72h-.72A8.87,8.87,0,0,1,304,55.55,12,12,0,0,1,297,57.41Zm18.22-.56h-7.25v-6.6l-.41-.11V40.42c0-1.81-.42-3-1.27-3.66s-2.3-.94-4.37-.94a7.38,7.38,0,0,0-4.25.94,3.87,3.87,0,0,0-1.29,3.33v.22h-7.81v-.16a10.91,10.91,0,0,1,1.7-6.08A11.33,11.33,0,0,1,295.07,30a17.23,17.23,0,0,1,7.38-1.47,15.14,15.14,0,0,1,7.16,1.5,9.66,9.66,0,0,1,4.2,4.19,13.86,13.86,0,0,1,1.37,6.35Z"
									/>
									<path d="M327.1,26.21h-7.77V19.66h7.77Zm0,30.64h-7.77V29h7.77Z" />
									<path
										d="M339,56.85h-7.76V29h7.19V37.7L339,38Zm20.91,0h-7.76V42.31c0-2.26-.49-3.88-1.45-4.86s-2.64-1.47-5-1.47-4.22.55-5.2,1.64S339,40.44,339,42.81h-1l-.57-5.22h1.45a12.84,12.84,0,0,1,1.55-4.41,9.19,9.19,0,0,1,3.39-3.39,10.9,10.9,0,0,1,5.62-1.3A10.75,10.75,0,0,1,355.31,30a9,9,0,0,1,3.47,4,13.31,13.31,0,0,1,1.14,5.6Z"
									/>
									<path
										class="cls-2"
										d="M44.92,76.52H31.52A17.8,17.8,0,0,1,13.76,58.73h7.66a10.12,10.12,0,0,0,10.1,10.13h13.4A10.13,10.13,0,0,0,51.39,51l-30.6-19c-.13-.08-.25-.17-.37-.26A17.79,17.79,0,0,1,31.52,0h13.4A17.79,17.79,0,0,1,62.68,17.78H55A10.12,10.12,0,0,0,44.92,7.66H31.52a10.12,10.12,0,0,0-6.47,17.89l30.59,19,.38.26a17.79,17.79,0,0,1-11.1,31.67Z"
									/>
									<path
										class="cls-2"
										d="M58.67,62.74V55.08A10.13,10.13,0,0,0,68.78,45V31.55a10.1,10.1,0,0,0-17.87-6.48L31.9,55.7c-.08.13-.17.25-.26.37A17.77,17.77,0,0,1,0,45V31.55A17.8,17.8,0,0,1,17.77,13.77v7.66A10.12,10.12,0,0,0,7.66,31.55V45a10.1,10.1,0,0,0,17.86,6.49l19-30.63a3.09,3.09,0,0,1,.26-.37,17.76,17.76,0,0,1,31.64,11.1V45A17.79,17.79,0,0,1,58.67,62.74Z"
									/>
								</g>
							</g>
						</svg>
					</Flex>
				</NuxtLink>
			</Flex>

			<Flex justify="center" align="center" wrap="wrap" gap="8" :class="$style.links">
				<NuxtLink to="/" :class="[$style.link, isActive('index') && $style.active]">
					<Text size="13" weight="600" color="tertiary">Explore</Text>
				</NuxtLink>

				<NuxtLink to="/txs" :class="[$style.link, isActive('txs') && $style.active]">
					<Text size="13" weight="600" color="tertiary">Transactions</Text>
				</NuxtLink>

				<NuxtLink to="/blocks" :class="[$style.link, isActive('blocks') && $style.active]">
					<Text size="13" weight="600" color="tertiary">Blocks</Text>
				</NuxtLink>

				<NuxtLink to="/validators" :class="[$style.link, isActive('validators') && $style.active]">
					<Text size="13" weight="600" color="tertiary">Validators</Text>
				</NuxtLink>
			</Flex>

			<Flex align="center" gap="8">
				<Dropdown>
					<Tooltip v-if="head" position="end">
						<Flex align="center" gap="8" :class="[$style.network]">
							<div :class="[$style.status, head.synced ? $style.green : $style.red]" />
							<Text size="12" weight="600" color="secondary" :class="$style.name"> {{ getNetworkName() }} </Text>
						</Flex>

						<template #content>
							<Text color="primary"><template v-if="!head.synced">Not</template> Synced </Text>
						</template>
					</Tooltip>

					<template #popup>
						<DropdownTitle>Network</DropdownTitle>
						<DropdownItem @click="handleNavigate('https://celenium.io')">Mainnet</DropdownItem>
						<DropdownItem @click="handleNavigate('https://mocha-4.celenium.io')">Mocha-4</DropdownItem>
						<DropdownItem @click="handleNavigate('https://arabica.celenium.io')">Arabica</DropdownItem>
					</template>
				</Dropdown>

				<Tooltip position="end" delay="250">
					<Button @click="appStore.showCmd = true" type="secondary" size="small">
						<Icon name="search" size="16" color="secondary" />
					</Button>

					<template #content>
						<Flex align="center" gap="8">
							Explore Celestia Blockchain
							<Flex align="center" gap="4">
								<Kbd>{{ isMac ? "Cmd" : "Ctrl" }}</Kbd>
								<Kbd>K</Kbd>
							</Flex>
						</Flex>
					</template>
				</Tooltip>

				<Connection :class="$style.connection_btn" />
			</Flex>
		</Flex>

		<Flex v-if="showPopup" @click="showPopup = false" direction="column" gap="8" :class="$style.menu_popup">
			<NuxtLink to="/" :class="[$style.link, isActive('index') && $style.active]">
				<Text size="13" weight="600" color="tertiary">Explore</Text>
			</NuxtLink>

			<NuxtLink to="/txs" :class="[$style.link, isActive('txs') && $style.active]">
				<Text size="13" weight="600" color="tertiary">Transactions</Text>
			</NuxtLink>

			<NuxtLink to="/blocks" :class="[$style.link, isActive('blocks') && $style.active]">
				<Text size="13" weight="600" color="tertiary">Blocks</Text>
			</NuxtLink>

			<NuxtLink to="/validators" :class="[$style.link, isActive('validators') && $style.active]">
				<Text size="13" weight="600" color="tertiary">Validators</Text>
			</NuxtLink>
		</Flex>
	</Flex>
</template>

<style module>
.wrapper {
	position: relative;

	height: 52px;
}

.container {
	max-width: var(--base-width);

	margin: 0 24px;
}

.logo {
	box-sizing: content-box;
	background: linear-gradient(225deg, #1e804d, #093a21);
	box-shadow: inset 0 0 0 1px var(--op-10);
	cursor: pointer;
	border-radius: 8px;

	padding: 6px;
}

.logo_name {
	fill: var(--logo-name);
}

.link {
	display: flex;
	align-items: center;

	height: 26px;

	background: transparent;
	border-radius: 50px;

	padding: 0 10px;

	transition: all 0.1s ease;

	&:hover {
		background: var(--op-5);

		& span {
			color: var(--txt-secondary);
		}
	}

	& span {
		transition: all 0.1s ease;
	}

	&.active {
		background: rgba(255, 255, 255, 90%);

		&:hover {
			background: rgba(255, 255, 255, 90%);

			& span {
				color: var(--txt-black);
			}
		}

		& span {
			color: var(--txt-black);
		}
	}
}

.menu_popup {
	position: absolute;
	top: 52px;
	left: 0;
	right: 0;

	display: none;

	background: var(--app-background);
	border-top: 2px solid var(--op-5);
	border-bottom: 2px solid var(--op-5);

	padding: 16px;

	z-index: 100;
}

.button {
	height: 28px;

	border-radius: 6px;
	background: var(--op-8);
	cursor: pointer;

	padding: 0 8px;

	transition: all 0.2s ease;

	&:hover {
		background: var(--op-8);
	}

	&:active {
		background: var(--op-10);
	}

	&.menu {
		display: none;
	}
}

.status {
	width: 5px;
	height: 5px;
	border-radius: 50px;

	&.green {
		background: var(--green);

		box-shadow: 0 0 6px var(--green);
	}

	&.red {
		background: var(--red);

		box-shadow: 0 0 6px var(--red);
	}
}

.network {
	height: 28px;

	border-radius: 8px;
	background: var(--op-5);
	box-shadow: inset 0 0 0 1px var(--op-5);

	padding: 0 12px;

	&:hover {
		.name {
			color: var(--txt-primary);
		}
	}
}

@media (max-width: 850px) {
	.links {
		display: none;
	}

	.button.menu {
		display: flex;
	}

	.menu_popup {
		display: flex;
	}
}

@media (max-width: 500px) {
	.container {
		margin: 0 12px;
	}

	.connection_btn {
		display: none;
	}
}

@media (max-width: 400px) {
	.logo_name {
		display: none;
	}
}
</style>
