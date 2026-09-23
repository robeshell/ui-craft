import SwiftUI

struct ChargerStatusView: View {
    @ObservedObject var model: ChargerModel

    var body: some View {
        VStack(spacing: 24) {
            HStack(alignment: .firstTextBaseline, spacing: 8) {
                Text(String(format: "%.1f", model.powerKW))
                    .font(.system(size: 64, weight: .semibold))
                Text("kW")
                    .font(.title2)
                    .foregroundColor(.secondary)
                Spacer()
                Button(action: model.togglePause) {
                    Image(systemName: model.isPaused ? "play.fill" : "pause.fill")
                        .font(.title)
                }
            }
            .padding(.horizontal, 20)

            HStack {
                Label("\(model.sessionMinutes) 分钟", systemImage: "clock")
                Spacer()
                Label(String(format: "%.2f kWh", model.energyKWh), systemImage: "bolt")
            }
            .font(.subheadline)
            .foregroundColor(.secondary)
            .padding(.horizontal, 20)

            Spacer()
        }
        .padding(.top, 32)
    }
}
