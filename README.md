# 🧠 Mạng Nơ-ron Tự Xây Dựng: Nhận Diện Chữ Viết Tay

Dự án này triển khai một mạng nơ-ron truyền thẳng (**Feedforward Neural Network**) từ đầu bằng **NumPy**, dùng để nhận diện chữ số viết tay (ví dụ: bộ dữ liệu MNIST).

![Kiến trúc mô hình](Images/2.png)

---

## 🏗️ Kiến trúc mô hình

- **Tầng đầu vào**: 784 nơ-ron (ảnh 28x28 được làm phẳng)
- **Tầng ẩn**: `n_1` nơ-ron (kèm hàm kích hoạt như `ReLU`, `tanh`)
- **Tầng đầu ra**: 10 nơ-ron (ứng với các chữ số từ 0 đến 9, dùng softmax)

---

## ⚙️ Các bước thực hiện

1. **Khởi tạo tham số ngẫu nhiên**
   - `W1`, `b1`, `W2`, `b2`

2. **Lan truyền xuôi (Forward Propagation)**
   - \( Z_1 = W_1 \cdot X + b_1 \)
   - \( A_1 = f(Z_1) \)
   - \( Z_2 = W_2 \cdot A_1 + b_2 \)
   - \( A_2 = \text{Softmax}(Z_2) \)

3. **Tính hàm mất mát (Loss)**
   - Dùng cross-entropy:
     \[
     Loss = -\sum y_k \cdot \log(a_k)
     \]

4. **Lan truyền ngược (Backward Propagation)**
   - Tính các đạo hàm: `dZ2`, `dW2`, `dB2`, `dZ1`, `dW1`, `dB1`

5. **Cập nhật tham số**
   - Dùng Gradient Descent:
     \[
     W = W - \alpha \cdot dW
     \]

---

## 📊 Đánh giá mô hình

- Tính **độ chính xác (accuracy)** trên tập huấn luyện và tập kiểm tra.
- Có thể thêm ma trận nhầm lẫn (confusion matrix) để trực quan hoá.

---

## 📁 Cấu trúc thư mục

