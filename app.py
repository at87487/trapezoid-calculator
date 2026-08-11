import gradio as gr
import math

def calculate_trapezoid_angles(group_no, height, no1_top, no1_bottom, no2_top, no2_bottom):
    if height <= 0:
        return f"【編號 {group_no}】錯誤：高度必須大於 0", ""
    
    def get_angle(top, bottom, name):
        if top <= 0 or bottom <= 0:
            return f"{name}: 上底與下底必須大於 0"
        if top == bottom:
            return f"{name}: 上底等於下底，這是矩形（底角為 90.0°）"
        
        base = abs(bottom - top) / 2.0
        radians = math.atan(height / base)
        degrees = math.degrees(radians)
        return f"{name} 底角為: {degrees:.2f}°"

    res_no1 = get_angle(no1_top, no1_bottom, "梯形 No.1")
    res_no2 = get_angle(no2_top, no2_bottom, "梯形 No.2")
    
    summary_title = f"📊 編號【{group_no}】計算結果："
    summary_content = f"▶ {res_no1}\n▶ {res_no2}"
    
    return summary_title, summary_content

# 建立 Gradio 美化介面
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📐 等腰梯形底角即時計算系統")
    gr.Markdown("請輸入數據編號、共用高度，並分別填入 No.1 與 No.2 梯形的上底和下底。")
    
    with gr.Row():
        with gr.Column(scale=1):
            group_no = gr.Textbox(label="數據編號", placeholder="例如: EXP-001", value="No.1")
            height = gr.Number(label="梯形高度 (共用)", value=10.0, minimum=0.1)
            btn = gr.Button("⚡ 馬上計算底角", variant="primary")
            
        with gr.Column(scale=2):
            with gr.Row():
                with gr.Group():
                    gr.Markdown("### 🔷 梯形 No.1")
                    no1_top = gr.Number(label="No.1 上底", value=5.0)
                    no1_bottom = gr.Number(label="No.1 下底", value=15.0)
                    
                with gr.Group():
                    gr.Markdown("### 🔶 梯形 No.2")
                    no2_top = gr.Number(label="No.2 上底", value=8.0)
                    no2_bottom = gr.Number(label="No.2 下底", value=12.0)

    gr.Markdown("---")
    with gr.Group():
        output_title = gr.Markdown("### 📋 點擊上方按鈕看計算結果")
        output_text = gr.Textbox(label="詳細角度數據", interactive=False, lines=3)

    btn.click(
        fn=calculate_trapezoid_angles,
        inputs=[group_no, height, no1_top, no1_bottom, no2_top, no2_bottom],
        outputs=[output_title, output_text]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
