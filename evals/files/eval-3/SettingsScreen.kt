package com.example.settings

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

data class SettingItem(val title: String, val subtitle: String?, val enabled: Boolean)

val SecondaryText = Color(0xFF9E9E9E)
val Divider = Color(0xFFEEEEEE)

@Composable
fun SettingsScreen(items: List<SettingItem>, onToggle: (SettingItem) -> Unit) {
    LazyColumn(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp)
    ) {
        item {
            Text("设置", fontSize = 16.sp, color = Color.Black)
        }
        items(items.size) { i ->
            val item = items[i]
            Card(
                modifier = Modifier.fillMaxWidth(),
                elevation = CardDefaults.cardElevation(defaultElevation = 4.dp)
            ) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(12.dp),
                    verticalAlignment = androidx.compose.ui.Alignment.CenterVertically
                ) {
                    Column(modifier = Modifier.weight(1f)) {
                        Text(item.title, fontSize = 16.sp, color = Color.Black)
                        if (item.subtitle != null) {
                            Text(item.subtitle, fontSize = 14.sp, color = SecondaryText)
                        }
                    }
                    Switch(checked = item.enabled, onCheckedChange = { onToggle(item) })
                }
                HorizontalDivider(color = Divider, thickness = 1.dp)
            }
        }
    }
}
