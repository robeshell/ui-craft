import SwiftUI

/// 会员套餐卡片。设计师标注见对话。
struct PlanCard: View {
    let title: String      // 如 "年度会员"
    let subtitle: String   // 如 "每月仅需 ¥16.5，立省 40%"
    let price: String      // 如 "¥198"
    let onSelect: () -> Void

    var body: some View {
        // TODO: 按设计标注实现
        EmptyView()
    }
}
