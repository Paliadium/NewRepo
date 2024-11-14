using System;

namespace GameNamespace
{
    // Интерфейс Attacker для объектов, которые могут атаковать
    public interface IAttacker
    {
        void Attack(Unit unit);
    }

    // Интерфейс Moveable для объектов, которые могут передвигаться
    public interface IMoveable
    {
        void Move(int newX, int newY);
    }

    // Базовый абстрактный класс для всех игровых объектов
    public abstract class GameObject
    {
        public int Id { get; }
        public string Name { get; }
        public int X { get; protected set; }
        public int Y { get; protected set; }

        public GameObject(int id, string name, int x, int y)
        {
            Id = id;
            Name = name;
            X = x;
            Y = y;
        }
    }

    // Абстрактный класс для юнитов
    public abstract class Unit : GameObject
    {
        public float Hp { get; protected set; }

        protected Unit(int id, string name, int x, int y, float hp)
            : base(id, name, x, y)
        {
            Hp = hp;
        }

        public bool IsAlive() => Hp > 0;

        public void ReceiveDamage(float damage)
        {
            Hp = Math.Max(Hp - damage, 0);
        }
    }

    // Класс Archer, реализует интерфейсы Attacker и Moveable
    public class Archer : Unit, IAttacker, IMoveable
    {
        public Archer(int id, string name, int x, int y, float hp)
            : base(id, name, x, y, hp) { }

        public void Attack(Unit unit)
        {
            Console.WriteLine($"{Name} атакует {unit.Name}!");
            unit.ReceiveDamage(10); // Условный урон
        }

        public void Move(int newX, int newY)
        {
            Console.WriteLine($"{Name} перемещается из ({X}, {Y}) в ({newX}, {newY})");
            X = newX;
            Y = newY;
        }
    }

    // Абстрактный класс для построек
    public abstract class Building : GameObject
    {
        public bool IsBuilt { get; protected set; }

        protected Building(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y)
        {
            IsBuilt = isBuilt;
        }
    }

    // Класс Fort, реализует интерфейс Attacker
    public class Fort : Building, IAttacker
    {
        public Fort(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y, isBuilt) { }

        public void Attack(Unit unit)
        {
            Console.WriteLine($"{Name} атакует {unit.Name} с помощью пушек!");
            unit.ReceiveDamage(20); // Условный урон
        }
    }

    // Класс MobileHouse, реализует интерфейс Moveable
    public class MobileHouse : Building, IMoveable
    {
        public MobileHouse(int id, string name, int x, int y, bool isBuilt)
            : base(id, name, x, y, isBuilt) { }

        public void Move(int newX, int newY)
        {
            Console.WriteLine($"{Name} перемещается из ({X}, {Y}) в ({newX}, {newY})");
            X = newX;
            Y = newY;
        }
    }

    // Тестирование
    public class Program
    {
        public static void Main()
        {
            Archer archer = new Archer(1, "Лучник", 0, 0, 100);
            Fort fort = new Fort(2, "Крепость", 5, 5, true);
            MobileHouse mobileHouse = new MobileHouse(3, "Дом на колёсах", 10, 10, true);

            // Тест передвижения и атаки
            archer.Move(3, 3);
            fort.Attack(archer);
            mobileHouse.Move(6, 6);

            Console.WriteLine($"Здоровье лучника: {archer.Hp}");
        }
    }
}
