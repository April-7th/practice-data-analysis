import csv

def analyze_sales(filename):
    products = []
    total_revenue = 0
    best_seller_product = ""
    max_quantity = 0

    print(f"--- ĐANG PHÂN TÍCH FILE: {filename} ---")

    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                product_name = row['Product']
                price = float(row['Price'])
                quantity = int(row['Quantity'])
                
                # 1. Tính doanh thu từng dòng
                revenue = price * quantity
                total_revenue += revenue
                
                # 2. Tìm sản phẩm bán chạy nhất (theo số lượng)
                if quantity > max_quantity:
                    max_quantity = quantity
                    best_seller_product = product_name
                
                print(f"- Đã xử lý: {product_name} (Doanh thu: ${revenue:,.2f})")

        print("\n" + "="*30)
        print("KẾT QUẢ PHÂN TÍCH:")
        print(f"1. Tổng doanh thu: ${total_revenue:,.2f}")
        print(f"2. Sản phẩm bán chạy nhất: {best_seller_product} (SL: {max_quantity})")
        print("="*30)

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file data.csv!")

# Chạy chương trình
if __name__ == "__main__":
    analyze_sales('data.csv')
