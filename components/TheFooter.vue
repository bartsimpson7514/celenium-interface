<script setup>
/** UI */
import { Dropdown, DropdownItem, DropdownTitle } from "@/components/ui/Dropdown"

/** Services */
import { isPrefersDarkScheme } from "@/services/utils"

/** Store */
import { useAppStore } from "@/store/app"
const appStore = useAppStore()

const appConfig = useAppConfig()

const theme = useCookie("theme", { default: () => "dark" })
switch (theme.value) {
	case "dark":
	case "dimmed":
	case "light":
		appStore.theme = theme.value

		break

	case "system":
		appStore.theme = "system"

		break
}

onMounted(() => {
	let root = document.querySelector("html")

	if (appStore.theme === "system") {
		root.setAttribute("theme", isPrefersDarkScheme() ? "dark" : "light")
	} else {
		root.setAttribute("theme", appStore.theme)
	}
})

watch(
	() => appStore.theme,
	() => {
		if (appStore.theme === "system") {
			window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (event) => {
				root.setAttribute("theme", isPrefersDarkScheme() ? "dark" : "light")
			})
		}
	},
)

const handleChangeTheme = (target) => {
	const root = document.querySelector("html")

	root.setAttribute("theme", target)
	appStore.theme = target
	theme.value = target
}
</script>

<template>
	<Flex tag="footer" justify="center" :class="$style.wrapper">
		<Flex justify="between" wide :class="$style.container">
			<Flex direction="column" gap="12">
				<Flex align="center" gap="8">
					<!-- <Icon name="logo" size="14" color="tertiary" /> -->

					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 260.27" style="height: 15px">
						<defs>
							<component :is="'style'">.cls-1 { fill: #5e3dff; }</component>
						</defs>
						<g id="Layer_2" data-name="Layer 2">
							<g id="Layer_1-2" data-name="Layer 1">
								<path
									class="cls-1"
									d="M152.78,260.27H107.22a60.52,60.52,0,0,1-60.43-60.48H72.85a34.43,34.43,0,0,0,34.37,34.42h45.56a34.44,34.44,0,0,0,22-60.86L70.73,108.6a12.42,12.42,0,0,1-1.26-.89A60.49,60.49,0,0,1,107.22,0h45.56a60.52,60.52,0,0,1,60.43,60.48H187.15a34.43,34.43,0,0,0-34.37-34.42H107.22a34.44,34.44,0,0,0-22,60.86l104.07,64.75a12.56,12.56,0,0,1,1.27.89,60.5,60.5,0,0,1-37.76,107.71Z"
								/>
								<path
									class="cls-1"
									d="M199.57,213.42v-26a34.44,34.44,0,0,0,34.37-34.43V107.32a34.36,34.36,0,0,0-60.75-22.06l-64.68,104.2a13.65,13.65,0,0,1-.89,1.26A60.42,60.42,0,0,1,0,152.94V107.32A60.52,60.52,0,0,1,60.43,46.84V72.9a34.43,34.43,0,0,0-34.37,34.42v45.62A34.36,34.36,0,0,0,86.81,175l64.68-104.2a13.65,13.65,0,0,1,.89-1.26A60.42,60.42,0,0,1,260,107.32v45.62A60.52,60.52,0,0,1,199.57,213.42Z"
								/>
							</g>
						</g>
					</svg>
					<Text size="13" weight="500" color="secondary">Self Chain</Text>
					<Text size="13" weight="500" color="tertiary">-</Text>
					<Text size="13" weight="500" color="tertiary">Self Chain Explorer</Text>
					<a :href="`https://docs.selfchain.xyz/learn/about-self-chain`" target="_blank">
						<Flex>
							<Text size="13" weight="500" color="support">v</Text>
							<Text size="13" weight="500" color="tertiary">{{ appConfig.version }}</Text>
						</Flex>
					</a>
				</Flex>

				<Flex align="center" gap="8">
					<NuxtLink to="https://www.frontier.xyz/terms-and-conditions" :class="$style.link">
						<Text size="12" weight="500" color="tertiary">Terms of Use</Text>
					</NuxtLink>
					<NuxtLink to="https://www.frontier.xyz/privacy-policy" :class="$style.link">
						<Text size="12" weight="500" color="tertiary">Privacy Policy</Text>
					</NuxtLink>
				</Flex>

				<Flex align="center" gap="8">
					<Text size="12" weight="500" color="support">Donations:</Text>
					<a :href="``" target="_blank">
						<Flex>
							<Text size="12" weight="500" color="tertiary">SLF</Text>
						</Flex>
					</a>
					<a :href="``" target="_blank">
						<Flex>
							<Text size="12" weight="500" color="tertiary">ETH</Text>
						</Flex>
					</a>
				</Flex>
			</Flex>
			<Flex direction="column" align="end" gap="16">
				<Flex align="center" gap="16">
					<Dropdown side="top">
						<Flex align="center" gap="6" :class="$style.btn">
							<Icon
								:name="
									appStore.theme
										? (appStore.theme === 'system' && 'settings') ||
										  (appStore.theme === 'light' && 'sun') ||
										  (['dark', 'dimmed'].includes(appStore.theme) && 'moon')
										: ''
								"
								size="12"
								color="secondary"
							/>
							<Text size="12" weight="600" color="secondary" :style="{ textTransform: 'capitalize' }">
								{{ appStore.theme }}
							</Text>
						</Flex>

						<template #popup>
							<DropdownTitle>Theme</DropdownTitle>
							<DropdownItem @click="handleChangeTheme('dimmed')">Dimmed</DropdownItem>
							<DropdownItem @click="handleChangeTheme('dark')">Dark</DropdownItem>
							<DropdownItem @click="handleChangeTheme('light')">Light</DropdownItem>
							<DropdownItem @click="handleChangeTheme('system')">System</DropdownItem>
						</template>
					</Dropdown>

					<Text size="12" weight="700" color="support">/</Text>

					<Flex align="center" gap="8" :class="$style.socials">
						<a href="https://twitter.com/selfchainxyz" target="_blank">
							<Icon name="twitter" size="14" color="secondary" :class="$style.btn" />
						</a>
						<a href="https://staking.selfchain.xyz/" target="_blank">
							<Icon name="coins" size="14" color="secondary" :class="$style.btn" />
						</a>
						<a href="https://discord.com/invite/selfchainxyz" target="_blank">
							<Icon name="discord" size="14" color="secondary" :class="$style.btn" />
						</a>
						<a href="https://t.me/selfchainxyz" target="_blank">
							<Icon name="telegram" size="14" color="secondary" :class="$style.btn" />
						</a>
					</Flex>
				</Flex>

				<Flex align="center" gap="16" :class="$style.links">
					<NuxtLink to="/blocks" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Blocks </Text>
					</NuxtLink>
					<NuxtLink to="/validators" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Validators </Text>
					</NuxtLink>
					<NuxtLink to="/txs" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Transactions </Text>
					</NuxtLink>
					<!-- <NuxtLink to="/rollups" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Rollups </Text>
					</NuxtLink> -->
					<!-- <NuxtLink to="/namespaces" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Namespaces </Text>
					</NuxtLink> -->
					<!-- <NuxtLink to="/addresses" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Addresses </Text>
					</NuxtLink> -->
					<!-- <NuxtLink to="/blobstream" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Blobstream </Text>
					</NuxtLink> -->
					<!-- <NuxtLink to="/gas" :class="$style.link">
						<Text size="12" weight="500" color="tertiary"> Gas Tracker </Text>
					</NuxtLink> -->
					<NuxtLink to="https://docs.selfchain.xyz/" :class="$style.link" target="_blank">
						<Text size="12" weight="500" color="tertiary"> Docs </Text>
					</NuxtLink>
				</Flex>
			</Flex>
		</Flex>
	</Flex>
</template>

<style module>
.wrapper {
	border-top: 2px solid var(--op-5);
}

.container {
	max-width: var(--base-width);

	padding: 24px 0;
	margin: 0 24px;
}

.link {
	& span {
		transition: all 0.2s ease;

		&:hover {
			color: var(--txt-primary);
		}
	}
}

.btn {
	box-sizing: content-box;
	border-radius: 5px;
	background: var(--op-8);
	cursor: pointer;

	padding: 6px;

	transition: all 0.2s ease;

	&:hover {
		background: var(--op-10);
	}

	&:active {
		background: var(--op-15);
	}
}

.socials {
	& a {
		display: flex;
	}
}

@media (max-width: 600px) {
	.container {
		flex-direction: column;
		gap: 12px;
	}

	.links {
		flex-wrap: wrap;
		justify-content: center;
	}
}
</style>
