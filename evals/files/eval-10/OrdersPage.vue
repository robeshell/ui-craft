<template>
  <div class="min-h-screen bg-[#F5F6F8] text-[#1A1A1A]">
    <header class="mx-auto flex max-w-6xl items-center justify-between px-8 pt-8">
      <h1 class="text-xl font-semibold">订单管理</h1>
      <button class="h-9 rounded-lg bg-[#2563EB] px-4 text-sm font-medium text-white hover:bg-[#1D4ED8] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#2563EB]/40">新建订单</button>
    </header>

    <main class="mx-auto max-w-6xl px-8 py-6">
      <section class="rounded-xl bg-white" aria-labelledby="orders-title">
        <div class="flex flex-wrap items-center gap-3 border-b border-[#E5E7EB] px-5 py-3">
          <h2 id="orders-title" class="text-sm font-semibold">待处理订单</h2>
          <span class="text-[13px] text-[#5C5C5C]">共 <span class="tabular-nums">{{ orders.length }}</span> 单</span>
          <div class="ml-auto flex gap-2">
            <button class="h-8 rounded-md border border-[#D1D5DB] bg-white px-3 text-sm text-[#1A1A1A] hover:bg-[#F5F6F8]">筛选</button>
            <button class="h-8 rounded-md border border-[#D1D5DB] bg-white px-3 text-sm text-[#1A1A1A] hover:bg-[#F5F6F8]">导出</button>
          </div>
        </div>

        <ul v-if="orders.length" class="divide-y divide-[#F0F1F3]">
          <li v-for="o in orders" :key="o.id" class="grid min-h-[48px] grid-cols-[112px_minmax(0,1fr)_96px_88px_96px] items-center gap-x-4 px-5 py-2">
            <span class="text-sm tabular-nums text-[#5C5C5C]">{{ o.id }}</span>
            <span class="truncate text-sm font-medium" :title="o.customer">{{ o.customer }}</span>
            <span class="text-right text-sm tabular-nums">¥{{ o.amount }}</span>
            <span class="flex items-center gap-1.5 text-[13px]" :class="o.urgent ? 'text-[#B91C1C]' : 'text-[#5C5C5C]'">
              <span class="h-1.5 w-1.5 rounded-full" :class="o.urgent ? 'bg-[#DC2626]' : 'bg-[#9CA3AF]'" aria-hidden="true"></span>
              {{ o.urgent ? '加急' : '普通' }}
            </span>
            <button class="h-8 justify-self-end rounded-md bg-[#2563EB] px-3 text-sm font-medium text-white hover:bg-[#1D4ED8]" @click="$emit('take', o)">接单</button>
          </li>
        </ul>
        <p v-else class="px-5 py-12 text-center text-sm text-[#5C5C5C]">暂无待处理订单</p>
      </section>
    </main>
  </div>
</template>

<script setup>
defineProps({ orders: { type: Array, default: () => [] } })
defineEmits(['take'])
</script>
