<script setup>
/** Vendor */
import { DateTime } from "luxon"

/** Services */
import { comma, formatBytes, abbreviate } from "@/services/utils"

/** UI */
import Tooltip from "@/components/ui/Tooltip.vue"

/** API */
import { fetchPriceSeries } from "@/services/api/stats"

/** Store */
import { useAppStore } from "@/store/app"
const appStore = useAppStore()

const head = computed(() => appStore.lastHead)
const currentPrice = computed(() => appStore.currentPrice)

const totalSupply = computed(() => head.value.total_supply / 1_000_000)
const totalSupplyUSD = computed(() => totalSupply.value * currentPrice.value?.close)
const totalFees = computed(() => head.value.total_fee / 1_000_000)
const totalFeesUSD = computed(() => totalFees.value * currentPrice.value?.close)

const series = ref([])
const price = reactive({
	value: 0,
	diff: 0,
	side: null,
})

onMounted(async () => {
	const dataSeries = await fetchPriceSeries({ from: parseInt(DateTime.now().minus({ days: 3 }).ts / 1_000) })
	series.value = dataSeries
	appStore.currentPrice = series.value[0]
	price.value = parseFloat(series.value[0].close)

	const prevDayClosePrice = parseFloat(series.value[1].close)
	price.diff = (Math.abs(prevDayClosePrice - price.value) / ((prevDayClosePrice + price.value) / 2)) * 100
	let side = "stay"
	if (price.value - prevDayClosePrice !== 0) {
		side = price.value - prevDayClosePrice > 0 ? "rise" : "fall"
	}
	price.side = side
})
</script>

<template>
	<Flex tag="section" justify="center" wide :class="$style.wrapper">
		<Flex align="center" justify="between" gap="24" wide :class="$style.container">
			<Flex align="center" gap="20" :class="$style.stats">
				<Tooltip>
					<Flex align="center" gap="6" :class="$style.stat">
						<Icon name="tx" size="12" color="secondary" :class="$style.icon" />
						<Flex align="center" gap="4">
							<Text size="12" weight="500" color="tertiary" noWrap :class="$style.key">Total Txs:</Text>

							<Text v-if="head" size="12" weight="600" noWrap :class="$style.value">{{ abbreviate(head.total_tx) }}</Text>
							<Skeleton v-else w="40" h="12" />
						</Flex>
					</Flex>

					<template #content>
						{{ comma(head.total_tx) }}
					</template>
				</Tooltip>

				<div :class="$style.dot" />

				<Tooltip>
					<Flex align="center" gap="6" :class="$style.stat">
						<Icon name="coins" size="12" color="secondary" :class="$style.icon" />
						<Flex align="center" gap="4">
							<Text size="12" weight="500" color="tertiary" noWrap :class="$style.key">Total Supply:</Text>

							<Text v-if="head" size="12" weight="600" noWrap :class="$style.value">
								{{ abbreviate(totalSupply, 2) }} SLF
							</Text>
							<Skeleton v-else w="55" h="12" />
						</Flex>
					</Flex>

					<template #content> {{ abbreviate(totalSupplyUSD, 2) }} USD </template>
				</Tooltip>

				<div :class="$style.dot" />

				<Tooltip>
					<Flex align="center" gap="6" :class="$style.stat">
						<Icon name="namespace" size="12" color="secondary" :class="$style.icon" />
						<Flex align="center" gap="4">
							<Text size="12" weight="500" color="tertiary" noWrap :class="$style.key">Total Blobs Size:</Text>

							<Text v-if="head" size="12" weight="600" noWrap :class="$style.value">{{
								formatBytes(head.total_blobs_size)
							}}</Text>
							<Skeleton v-else w="60" h="12" />
						</Flex>
					</Flex>

					<template #content> {{ comma(head.total_blobs_size) }} Bytes</template>
				</Tooltip>

				<div :class="$style.dot" />

				<Tooltip>
					<Flex align="center" gap="6" :class="$style.stat">
						<Icon name="tag" size="12" color="secondary" :class="$style.icon" />
						<Flex align="center" gap="4">
							<Text size="12" weight="500" color="tertiary" noWrap :class="$style.key">Total Fees:</Text>

							<Text v-if="head" size="12" weight="600" noWrap :class="$style.value">
								{{ abbreviate(parseInt(totalFees)) }} SLF
							</Text>
							<Skeleton v-else w="55" h="12" />
						</Flex>
					</Flex>

					<template #content> {{ abbreviate(totalFeesUSD) }} USD </template>
				</Tooltip>
			</Flex>

			<Tooltip position="end">
				<Flex align="center" gap="6" :class="$style.stat">
					<Icon name="coin" size="12" color="secondary" :class="$style.icon" />

					<Flex align="center" gap="4">
						<Text size="12" weight="500" color="tertiary" noWrap :class="$style.key">SLF:</Text>

						<Text v-if="price.value" size="12" weight="600" noWrap :class="$style.value"> ${{ price.value.toFixed(2) }} </Text>
						<Skeleton v-else w="36" h="12" />
					</Flex>

					<Flex v-if="!isNaN(price.diff)" align="center" gap="4">
						<Icon v-if="price.side === 'rise'" name="arrow-circle-right-up" size="12" color="neutral-green" />
						<Icon v-else-if="price.side === 'fall'" name="arrow-circle-right-down" size="12" color="red" />

						<Text size="12" weight="600" :color="price.side === 'fall' ? 'red' : 'neutral-green'" noWrap>
							{{ price.diff.toFixed(2) }}%</Text
						>
					</Flex>
					<Skeleton v-else w="50" h="12" />
				</Flex>

				<template #content>
					<Flex direction="column" gap="6">
						<Flex align="center" gap="4">
							<Text color="primary">Price diff from the previous day</Text>
						</Flex>

						<Flex v-if="series.length" align="center" gap="4">
							<Text color="tertiary">{{ DateTime.fromISO(series[1].time).setLocale("en").toFormat("ff") }} -></Text>
							<Text color="primary">${{ parseFloat(series[1].close).toFixed(2) }}</Text>
						</Flex>

						<Flex align="center" gap="4">
							<Text size="11" color="tertiary">Binance quotes</Text>
						</Flex>
					</Flex>
				</template>
			</Tooltip>
		</Flex>
	</Flex>
</template>

<style module>
.wrapper {
	height: 32px;

	border-top: 1px solid var(--op-5);
	border-bottom: 1px solid var(--op-5);

	background: var(--feed-background);
}

.container {
	max-width: var(--base-width);
	height: 100%;

	margin: 0 24px;

	&::-webkit-scrollbar {
		display: none;
	}
}

.dot {
	width: 4px;
	height: 4px;
	background-color: var(--op-10);
	border-radius: 50%;
}

.key,
.value,
.icon {
	transition: all 0.2s ease;
}

.value {
	color: var(--op-40);
}

.stat:hover {
	.icon {
		fill: var(--txt-primary);
	}

	.key {
		color: var(--txt-secondary);
	}

	.value {
		color: var(--txt-secondary);
	}
}

@media (max-width: 900px) {
	.wrapper {
		height: initial;

		padding: 12px 0;
	}

	.container {
		flex-direction: column;
	}

	.stats {
		width: 100%;
		justify-content: center;
		flex-wrap: wrap;
	}
}

@media (max-width: 500px) {
	.container {
		margin: 0 12px;
	}
}
</style>
