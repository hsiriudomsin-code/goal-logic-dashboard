import pandas as pd
import numpy as np

# 1. ฐานข้อมูลรายชื่อนักเตะที่คุณส่งมา (ครบ 20 ทีม)
real_players = [
    # Manchester United
    {'ชื่อนักเตะ': 'Onana', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Dalot', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Varane', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Lisandro Martínez', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Shaw', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Casemiro', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Bruno Fernandes', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Mount', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Antony', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Højlund', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Rashford', 'ทีม': 'Man Utd', 'ตำแหน่ง': 'FW'},

    # Manchester City
    {'ชื่อนักเตะ': 'Ederson', 'ทีม': 'Man City', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Walker', 'ทีม': 'Man City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Dias', 'ทีม': 'Man City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Gvardiol', 'ทีม': 'Man City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Aké', 'ทีม': 'Man City', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Rodri', 'ทีม': 'Man City', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'De Bruyne', 'ทีม': 'Man City', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Bernardo Silva', 'ทีม': 'Man City', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Foden', 'ทีม': 'Man City', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Haaland', 'ทีม': 'Man City', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Doku', 'ทีม': 'Man City', 'ตำแหน่ง': 'FW'},

    # Liverpool
    {'ชื่อนักเตะ': 'Alisson', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Alexander-Arnold', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Konaté', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Van Dijk', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Robertson', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Mac Allister', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Szoboszlai', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Curtis Jones', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Salah', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Núñez', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Luis Díaz', 'ทีม': 'Liverpool', 'ตำแหน่ง': 'FW'},

    # Arsenal
    {'ชื่อนักเตะ': 'Raya', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'White', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Saliba', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Gabriel', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Zinchenko', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Rice', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Ødegaard', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Havertz', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Saka', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Jesus', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Martinelli', 'ทีม': 'Arsenal', 'ตำแหน่ง': 'FW'},

    # Chelsea
    {'ชื่อนักเตะ': 'Petrovic', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Reece James', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Disasi', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Colwill', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Chilwell', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Caicedo', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Enzo Fernández', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Gallagher', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Palmer', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Jackson', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Mudryk', 'ทีม': 'Chelsea', 'ตำแหน่ง': 'FW'},

    # Spurs
    {'ชื่อนักเตะ': 'Vicario', 'ทีม': 'Spurs', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Porro', 'ทีม': 'Spurs', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Romero', 'ทีม': 'Spurs', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Van de Ven', 'ทีม': 'Spurs', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Udogie', 'ทีม': 'Spurs', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Bissouma', 'ทีม': 'Spurs', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Maddison', 'ทีม': 'Spurs', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Sarr', 'ทีม': 'Spurs', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Kulusevski', 'ทีม': 'Spurs', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Son', 'ทีม': 'Spurs', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Richarlison', 'ทีม': 'Spurs', 'ตำแหน่ง': 'FW'},

    # Newcastle
    {'ชื่อนักเตะ': 'Pope', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Trippier', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Schär', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Botman', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Burn', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Guimarães', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Joelinton', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Longstaff', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Almirón', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Isak', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Gordon', 'ทีม': 'Newcastle', 'ตำแหน่ง': 'FW'},

    # Aston Villa
    {'ชื่อนักเตะ': 'Emiliano Martínez', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Cash', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Konsa', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Pau Torres', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Digne', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Kamara', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Douglas Luiz', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'McGinn', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Bailey', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Watkins', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Diaby', 'ทีม': 'Aston Villa', 'ตำแหน่ง': 'FW'},

    # Wolves
    {'ชื่อนักเตะ': 'José Sá', 'ทีม': 'Wolves', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Semedo', 'ทีม': 'Wolves', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Kilman', 'ทีม': 'Wolves', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Dawson', 'ทีม': 'Wolves', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Aït-Nouri', 'ทีม': 'Wolves', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Lemina', 'ทีม': 'Wolves', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'João Gomes', 'ทีม': 'Wolves', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Sarabia', 'ทีม': 'Wolves', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Neto', 'ทีม': 'Wolves', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Cunha', 'ทีม': 'Wolves', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Hwang Hee-chan', 'ทีม': 'Wolves', 'ตำแหน่ง': 'FW'},

    # Brentford
    {'ชื่อนักเตะ': 'Flekken', 'ทีม': 'Brentford', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Hickey', 'ทีม': 'Brentford', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Collins', 'ทีม': 'Brentford', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Pinnock', 'ทีม': 'Brentford', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Henry', 'ทีม': 'Brentford', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Nørgaard', 'ทีม': 'Brentford', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Jensen', 'ทีม': 'Brentford', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Janelt', 'ทีม': 'Brentford', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Mbeumo', 'ทีม': 'Brentford', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Toney', 'ทีม': 'Brentford', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Wissa', 'ทีม': 'Brentford', 'ตำแหน่ง': 'FW'},

    # Brighton
    {'ชื่อนักเตะ': 'Steele', 'ทีม': 'Brighton', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Veltman', 'ทีม': 'Brighton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Dunk', 'ทีม': 'Brighton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Van Hecke', 'ทีม': 'Brighton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Estupiñán', 'ทีม': 'Brighton', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Gross', 'ทีม': 'Brighton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Gilmour', 'ทีม': 'Brighton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'João Pedro', 'ทีม': 'Brighton', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Mitoma', 'ทีม': 'Brighton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Ferguson', 'ทีม': 'Brighton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Adingra', 'ทีม': 'Brighton', 'ตำแหน่ง': 'FW'},

    # West Ham
    {'ชื่อนักเตะ': 'Areola', 'ทีม': 'West Ham', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Coufal', 'ทีม': 'West Ham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Zouma', 'ทีม': 'West Ham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Aguerd', 'ทีม': 'West Ham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Emerson', 'ทีม': 'West Ham', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Ward-Prowse', 'ทีม': 'West Ham', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Álvarez', 'ทีม': 'West Ham', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Paquetá', 'ทีม': 'West Ham', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Bowen', 'ทีม': 'West Ham', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Antonio', 'ทีม': 'West Ham', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Kudus', 'ทีม': 'West Ham', 'ตำแหน่ง': 'FW'},

    # Crystal Palace
    {'ชื่อนักเตะ': 'Johnstone', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Clyne', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Andersen', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Guéhi', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Mitchell', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Lerma', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Doucouré', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Eze', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Olise', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Mateta', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Ayew', 'ทีม': 'Crystal Palace', 'ตำแหน่ง': 'FW'},

    # Everton
    {'ชื่อนักเตะ': 'Pickford', 'ทีม': 'Everton', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Patterson', 'ทีม': 'Everton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Tarkowski', 'ทีม': 'Everton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Branthwaite', 'ทีม': 'Everton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Mykolenko', 'ทีม': 'Everton', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Onana', 'ทีม': 'Everton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Garner', 'ทีม': 'Everton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Doucouré', 'ทีม': 'Everton', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Harrison', 'ทีม': 'Everton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Calvert-Lewin', 'ทีม': 'Everton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'McNeil', 'ทีม': 'Everton', 'ตำแหน่ง': 'FW'},

    # Fulham
    {'ชื่อนักเตะ': 'Leno', 'ทีม': 'Fulham', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Castagne', 'ทีม': 'Fulham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Ream', 'ทีม': 'Fulham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Adarabioyo', 'ทีม': 'Fulham', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Robinson', 'ทีม': 'Fulham', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Palhinha', 'ทีม': 'Fulham', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Pereira', 'ทีม': 'Fulham', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Reed', 'ทีม': 'Fulham', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Willian', 'ทีม': 'Fulham', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Jiménez', 'ทีม': 'Fulham', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Iwobi', 'ทีม': 'Fulham', 'ตำแหน่ง': 'FW'},

    # Nottm Forest
    {'ชื่อนักเตะ': 'Turner', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Aurier', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Niakhaté', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Murillo', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Aina', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Danilo', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Mangala', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Gibbs-White', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Elanga', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Awoniyi', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Hudson-Odoi', 'ทีม': 'Nottm Forest', 'ตำแหน่ง': 'FW'},

    # Bournemouth
    {'ชื่อนักเตะ': 'Neto', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Smith', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Zabarnyi', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Senesi', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Kerkez', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Cook', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Christie', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Billing', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Tavernier', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Solanke', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Kluivert', 'ทีม': 'Bournemouth', 'ตำแหน่ง': 'FW'},

    # Ipswich Town (ใช้ชื่อ Luton Town ตามลิสต์ทีมในโค้ดเดิม)
    {'ชื่อนักเตะ': 'Kaminski', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Osho', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Lockyer', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Bell', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Kabore', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Barkley', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Nakamba', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Doughty', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Townsend', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Morris', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Adebayo', 'ทีม': 'Ipswich Town', 'ตำแหน่ง': 'FW'},

    # Southampton (ใช้ชื่อ Burnley ตามลิสต์ทีมในโค้ดเดิม)
    {'ชื่อนักเตะ': 'Trafford', 'ทีม': 'Southampton', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Roberts', 'ทีม': 'Southampton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'O’Shea', 'ทีม': 'Southampton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Beyer', 'ทีม': 'Southampton', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Taylor', 'ทีม': 'Southampton', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Cullen', 'ทีม': 'Southampton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Brownhill', 'ทีม': 'Southampton', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Berge', 'ทีม': 'Southampton', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Koleosho', 'ทีม': 'Southampton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Foster', 'ทีม': 'Southampton', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'Amdouni', 'ทีม': 'Southampton', 'ตำแหน่ง': 'FW'},

    # Leicester City (ใช้ชื่อ Sheffield United ตามลิสต์ทีมในโค้ดเดิม)
    {'ชื่อนักเตะ': 'Foderingham', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'GK'},
    {'ชื่อนักเตะ': 'Baldock', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Ahmedhodzic', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Robinson', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Trusty', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'DF'}, {'ชื่อนักเตะ': 'Lowe', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'DF'},
    {'ชื่อนักเตะ': 'Hamer', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Souza', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'MF'}, {'ชื่อนักเตะ': 'Norwood', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'MF'},
    {'ชื่อนักเตะ': 'Archer', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'FW'}, {'ชื่อนักเตะ': 'McBurnie', 'ทีม': 'Leicester City', 'ตำแหน่ง': 'FW'},
]

# 2. ฟังก์ชันสุ่มสถิติ (Match Stats)
def add_stats(row):
    pos = row['ตำแหน่ง']
    if pos == 'GK':
        row['เซฟลูก'] = np.random.randint(2, 10)
        row['ประตู'] = 0
        row['แอสซิสต์'] = 0
        row['ระยะวิ่ง (กม.)'] = round(np.random.uniform(4.0, 6.0), 1)
    else:
        row['เซฟลูก'] = 0
        row['ประตู'] = np.random.randint(0, 3)
        row['แอสซิสต์'] = np.random.randint(0, 2)
        row['ระยะวิ่ง (กม.)'] = round(np.random.uniform(9.0, 12.5), 1)

    row['ใบเหลือง'] = np.random.choice([0, 1], p=[0.8, 0.2])
    score_now = (row['ประตู'] * 4) + (row['แอสซิสต์'] * 2) + (row['เซฟลูก'] * 1.0) + row['ระยะวิ่ง (กม.)'] - (row['ใบเหลือง'] * 2)
    row['คะแนนรวม'] = round(score_now, 1)
    row['คะแนนครั้งก่อน'] = max(0, round(score_now + np.random.uniform(-5, 5), 1))
    return row

# สร้าง DataFrame และบันทึก
df = pd.DataFrame(real_players)
df = df.apply(add_stats, axis=1)

file_name = 'EPL_Real_11_Lineups.xlsx'
df.to_excel(file_name, index=False)

print(f"✅ สำเร็จ! ไฟล์ '{file_name}'  {len(df)} คน")