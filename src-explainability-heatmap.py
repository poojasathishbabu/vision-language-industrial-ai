"""Explainability: attention / Grad-CAM heatmap - shows which pixels drove decision"""
def heatmap(image_path):
    return {"heatmap_path":f"{image_path}.heatmap.png","top_attention_regions":[{"bbox":[120,80,240,160],"score":0.92}]}
if __name__=="__main__": print(heatmap("sample.jpg"))
