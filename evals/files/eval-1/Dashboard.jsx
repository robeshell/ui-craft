import React from "react";

const Card = ({ title, children }) => (
  <div className="bg-white border border-gray-300 rounded-lg p-4 shadow-sm">
    <h2 className="text-lg font-bold text-gray-900 mb-3">{title}</h2>
    {children}
  </div>
);

export default function Dashboard({ metrics, alerts, services }) {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-2xl font-bold text-[#0F766E] mb-6">运维监控平台</h1>
      <div className="grid grid-cols-3 gap-4">
        <Card title="CPU 使用率">
          <p className="text-3xl text-[#0F766E]">{metrics.cpu}%</p>
          <p className="text-sm text-gray-400">最近 5 分钟平均</p>
        </Card>
        <Card title="内存">
          <p className="text-3xl text-[#0F766E]">{metrics.mem}%</p>
          <p className="text-sm text-gray-400">{metrics.memUsed} / {metrics.memTotal} GB</p>
        </Card>
        <Card title="磁盘">
          <p className="text-3xl text-[#0F766E]">{metrics.disk}%</p>
          <p className="text-sm text-gray-400">{metrics.diskUsed} / {metrics.diskTotal} TB</p>
        </Card>
        <Card title="最近告警">
          <ul>
            {alerts.slice(0, 3).map((a) => (
              <li key={a.id} className="text-sm text-gray-700 py-1">
                <span className={a.level === "critical" ? "text-red-500" : "text-yellow-500"}>●</span>{" "}
                {a.service} {a.message} <span className="text-gray-400">{a.time}</span>
              </li>
            ))}
          </ul>
        </Card>
        <Card title="服务列表">
          <ul>
            {services.slice(0, 4).map((s) => (
              <li key={s.name} className="text-sm text-gray-700 py-1 flex justify-between">
                <span>{s.name}</span>
                <span className={s.status === "up" ? "text-green-500" : "text-red-500"}>{s.status}</span>
              </li>
            ))}
          </ul>
        </Card>
        <Card title="快捷操作">
          <div className="flex flex-wrap gap-2">
            <button className="bg-[#0F766E] text-white px-3 py-1 rounded">重启服务</button>
            <button className="bg-[#0F766E] text-white px-3 py-1 rounded">查看日志</button>
            <button className="bg-[#0F766E] text-white px-3 py-1 rounded">静默告警</button>
            <button className="bg-[#0F766E] text-white px-3 py-1 rounded">导出报表</button>
          </div>
        </Card>
      </div>
    </div>
  );
}
