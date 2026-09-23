import React from "react";
import { View, Text, FlatList, Pressable, StyleSheet } from "react-native";

export type Device = {
  id: string;
  name: string;        // 用户命名，如 "客厅空气净化器"
  model: string;       // 型号，如 "AP-300"
  online: boolean;
};

type Props = {
  devices: Device[];   // 新用户通常只有 0 到 1 台
  onAdd: () => void;
  onOpen: (d: Device) => void;
};

export default function DevicesScreen({ devices, onAdd, onOpen }: Props) {
  return (
    <View style={styles.page}>
      <Text style={styles.title}>我的设备</Text>
      <FlatList
        data={devices}
        keyExtractor={(d) => d.id}
        ListEmptyComponent={<Text style={styles.empty}>暂无设备</Text>}
        renderItem={({ item }) => (
          <Pressable style={styles.row} onPress={() => onOpen(item)}>
            <Text style={styles.name}>{item.name}</Text>
            <Text style={styles.meta}>{item.model} · {item.online ? "在线" : "离线"}</Text>
          </Pressable>
        )}
      />
      <Pressable style={styles.add} onPress={onAdd}>
        <Text style={styles.addText}>添加设备</Text>
      </Pressable>
    </View>
  );
}

const styles = StyleSheet.create({
  page: { flex: 1, backgroundColor: "#fff", padding: 16 },
  title: { fontSize: 18, fontWeight: "600", marginBottom: 12 },
  empty: { color: "#999", marginTop: 40, textAlign: "center" },
  row: { paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: "#eee" },
  name: { fontSize: 16 },
  meta: { fontSize: 13, color: "#888", marginTop: 4 },
  add: { marginTop: 16, backgroundColor: "#1E90FF", borderRadius: 8, padding: 14, alignItems: "center" },
  addText: { color: "#fff", fontSize: 16 },
});
